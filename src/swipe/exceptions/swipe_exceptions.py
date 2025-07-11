class ProcessingBrokerMessageError(Exception):
    def __init__(self, error: str):
        self.detail = f"Error processing message: {error}"
