from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    def __init__(self, dataset):
        self.dataset = dataset
        assert "UID" in self.dataset.columns, "Dataset does not contain UID column"

    @property
    def result_column_name(self):
        """
        Generates a consistent result column name based on the class name or a predefined format.
        Named is in a format of <strategy_name>_result.
        """
        # Example: Convert class name to lowercase and replace underscores with spaces
        return f"{self.__class__.__name__.lower().replace('_', ' ')}_result"

    @abstractmethod
    def process_data(self):
        """
        Process the dataset. The implementation can vary depending on whether the strategy prefers individual rows, batches, or the entire dataset.
        Returns the processed dataset.
        """
        pass