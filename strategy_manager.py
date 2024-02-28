class StrategyManager:
    def __init__(self):
        self.strategies = {}

    def register_strategy(self, name, strategy_cls, description=""):
        self.strategies[name] = {"class": strategy_cls, "description": description}

    def get_strategy_description(self, name):
        return self.strategies.get(name, {}).get("description", "No description available.")


    def execute_strategy(self, name, dataset):
        strategy_cls = self.strategies.get(name)
        if not strategy_cls:
            raise ValueError("Strategy not found")
        strategy = strategy_cls(dataset)
        return strategy.process_data()
    
    def execute_strategies(self, names, dataset):
        results = {}
        for name in names:
            if name in self.strategies:
                results[name] = self.execute_strategy(name, dataset)
            else:
                results[name] = "Strategy not found"
        return results

    
    def list_strategies(self):
        return list(self.strategies.keys())

