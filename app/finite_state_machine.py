from aiogram.fsm.state import StatesGroup, State


class ConvertState(StatesGroup):
    choose_source_format = State()
    choose_target_format = State()
    wait_for_state = State()