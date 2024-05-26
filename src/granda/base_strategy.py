from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    """
    Base class for all strategies. All strategies should inherit from this class.
    Each strategy is create with a configuration dictionary and has a result column name.
    """

    def __init__(self, config):
        self.config = config
        self.in_tokens_count = 0
        self.out_tokens_count = 0

    @property
    def result_column_name(self):
        """
        Generates a consistent result column name based on the class name or a predefined format.
        Named is in a format of <strategy_name>_result.
        """
        # Example: Convert class name to lowercase and replace underscores with spaces
        return f"{self.model}_{self.__class__.__name__.lower().replace('_', ' ')}_result"

    @abstractmethod
    def process_data(self, dataset):
        """
        Process the dataset. The implementation can vary depending on whether the strategy prefers individual rows, batches, or the entire dataset.
        Returns the processed dataset.
        """
        assert "UID" in self.dataset.columns, "Dataset does not contain UID column"
        pass
