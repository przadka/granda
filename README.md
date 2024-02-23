# Granda Framework

Granda is a flexible evaluation framework designed to test and compare different LLM architectures easily. It allows strategies to process ground truth data either individually, in batches, or as a whole, making Granda agnostic to the consumption method of the ground truth data.

## Features

- Abstract strategy interface for easy implementation of new evaluation strategies.
- Strategy Manager for registering and executing strategies dynamically.
- Support for individual, batch, and whole dataset processing methods.

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or later installed on your system.

### Installation

1. Clone the Granda repository:

    ```bash
    git clone https://github.com/przadka/granda.git
    ```

2. Navigate to the Granda directory:

    ```bash
    cd granda
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use Granda, you need to define your strategies as subclasses of the `BaseStrategy` and then register them with the `StrategyManager`.

### Defining a Strategy

```python
from src.base_strategy import BaseStrategy

class MyStrategy(BaseStrategy):
    def process_data(self):
        # Implementation for processing data
        pass
```

### Registering and Executing a Strategy

```python
from src.strategy_manager import StrategyManager

manager = StrategyManager()
manager.register_strategy('my_strategy', MyStrategy)

# Assuming `dataset` is your DataFrame or data structure holding the ground truth data
results = manager.execute_strategy('my_strategy', dataset)
```

### Working with a Test Dataset

Granda expects only 2 columns in the dataset: `id` and `truth`. The first is id of your row with particular test case, and the the second is the expected value. You can organize your dataset however you want and add many other variables that are relevant, and that you may use when implementing a strategy. Granda will always keep them in the dataset.

TODO: explain how restults from executing strategy are stored.

TODO: where to store the results?


## Plans

- metrics, graphs

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

X/Twitter: [@przadka](https://x.com/przadka) - przadka@przadka.com

Github: [https://github.com/yourusername/granda](https://github.com/yourusername/granda)