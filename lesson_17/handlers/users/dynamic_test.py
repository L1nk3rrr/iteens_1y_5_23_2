from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import types
from aiogram.fsm.state import State, StatesGroup
from loader import dp, bot, db_users, ques



class FSMInitTest(StatesGroup):
    start_of_test = State()
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    final_q = State()

def dynamic_reply_db(answers: list):
    return types.ReplyKeyboardMarkup(
        keyboard = [
            [types.KeyboardButton(text=answer) for answer in answers] 
        ], resize_keyboard=True
    )

def question_generator(prev_number,curr_number, state_name, next_state):
    @dp.message(state_name, F.text.in_(ques[prev_number]['answers'].split('@')))
    async def question(msg: types.Message, state: FSMContext):
        our_data = await state.get_data()
        if msg.text == ques[prev_number]["right_answer"]:
            await state.update_data(
                {
                    "score":our_data['score'] + ques[prev_number]["point"],
                    f"answer_{prev_number}": f"Y Ви відповіли правильно! Відповідь: {ques[prev_number]['right_answer']}"
                }

            )
        else:
            await state.update_data(
                {
                    f"answer_{prev_number}": f"X Ви відповіли НЕправильно! Правильно Відповідь: {ques[prev_number]['right_answer']}"
                }

            )
        
        await msg.answer(f"Відповідь зарахована")
        await msg.answer(f"{curr_number} Питання:")
        await msg.answer(ques[curr_number]["question"], reply_markup=dynamic_reply_db(ques[curr_number]["answers"].split('@')))
        await state.set_state(next_state)

def init_questions():
    question_generator(1, 2, FSMInitTest.q2, FSMInitTest.q3)
    question_generator(2, 3, FSMInitTest.q3, FSMInitTest.final_q)


@dp.message(Command("my_test"))
async def my_test(msg: types.Message, state: FSMContext):
    if db_users.user_exists(msg.from_user.id) is not None:
        await msg.answer("Привіт, починаємо тест!")
        await state.update_data(score=0)
        await msg.answer(f"1 Питання:")
        await msg.answer(ques[1]["question"], reply_markup=dynamic_reply_db(ques[1]["answers"].split('@')))
        await state.set_state(FSMInitTest.q2)
    else:
        await msg.answer("Зареєструйся!")

@dp.message(FSMInitTest.final_q)
async def my_test(msg: types.Message, state: FSMContext):
    our_data = await state.get_data()

    score = our_data['score']
    english_level = "A1"
    if score == 0:
        await msg.answer("У тебе A0, біжи вчитись!")
    elif score > 5:
        ...
        english_level = "A2"
    elif score > 10:
        english_level = "B2"
        ...
    # db_user.update_english_level(english_level) # Це запис в бд рівня англ
    await msg.answer(f"Тест закінчено! Твій рівень {english_level}\nТвій результат - {score}/{len(ques)}", reply_markup=types.ReplyKeyboardRemove())
