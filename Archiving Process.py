import azure.functions as func

def main(timer: func.TimerRequest) -> None:
    archive_old_records()
