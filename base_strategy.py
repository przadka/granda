from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    def __init__(self, dataset):
        self.dataset = dataset
    
    @abstractmethod
    def process_data(self):
        """Process the dataset. The implementation can vary depending on whether the strategy prefers individual rows, batches, or the entire dataset."""
        pass
