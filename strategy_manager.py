from typing import Dict, List, Any

class StrategyManager:
    def __init__(self):
        self.strategies: Dict[str, Dict[str, Any]] = {}

    def register_strategy(self, name: str, strategy_cls: Any, description: str = "") -> None:
        """Register a new strategy with a name, class, and optional description."""
        self.strategies[name] = {"class": strategy_cls, "description": description}

    def get_strategy_description(self, name: str) -> str:
        """Get the description of a strategy by name, returning a default message if not found."""
        return self.strategies.get(name, {}).get("description", "No description available.")

    def execute_strategy(self, name: str, dataset: Any) -> Any:
        """Execute a strategy by name on the given dataset, raising an error if the strategy is not found."""
        strategy_info = self.strategies.get(name)
        if not strategy_info:
            raise ValueError(f"Strategy '{name}' not found")
        strategy = strategy_info['class'](dataset)
        return strategy.process_data()

    def execute_strategies(self, names: List[str], dataset: Any) -> Dict[str, Any]:
        """Execute multiple strategies by name on the given dataset, collecting results or errors."""
        results: Dict[str, Any] = {}
        for name in names:
            try:
                results[name] = self.execute_strategy(name, dataset)
            except ValueError as e:
                results[name] = str(e)
        return results

    def list_strategies(self) -> List[str]:
        """List the names of all registered strategies."""
        return list(self.strategies.keys())
