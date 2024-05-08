from typing import Dict, List, Any

from base_strategy import BaseStrategy


class StrategyManager:
    """
    Manages a collection of strategies, allowing them to be registered, executed, and listed.
    """

    def __init__(self):
        self.strategies = {}
    
    def register_strategy(self, strategy: BaseStrategy, name: str,  description: str = "") -> None:
        """Register a new strategy with the manager. Strategy is an instance of BaseStrategy."""
        self.strategies[name] = strategy

    def get_strategy_description(self, name: str) -> str:
        """Get the description of a strategy by name, returning a default message if not found."""
        strategy = self.strategies.get(name)
        return strategy.get("description", "No description available")
    
    def execute_strategy(self, name: str, dataset: Any) -> Any:
        """Execute a strategy by name on the given dataset, raising an error if the strategy is not found."""
        strategy = self.strategies.get(name)
        if strategy is None:
            raise ValueError(f"Strategy '{name}' not found")
        return strategy.process_data(dataset)
    
    def execute_strategies(self, names: List[str], dataset: Any) -> Dict[str, Any]:
        """Execute multiple strategies by name on the given datase. 
        Chain executions, passing the result of one strategy to the next, if needed. 
        Return a the object return by the last strategy, or an error message if the strategy fails."""
        result = dataset
        for name in names:
            result = self.execute_strategy(name, result)
        return result
    
    def list_strategies(self) -> List[str]:
        """List the names of all registered strategies."""
        return list(self.strategies.keys())
