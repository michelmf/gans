"""
Example of a pytorch code (testing purposes)
"""
import torch #type: ignore
from torch import nn

class LogisticRegression(nn.Module):
    """
    Class to define a logistic regression model.
    """
    def __init__(self, input_size: int) -> None:
        """
        Constructor of the class.
        """
        super().__init__()
        self.logistic_regression = nn.Sequential(
            nn.Linear(input_size, 1),
            nn.Sigmoid()
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass of the model.
        """
        return self.logistic_regression(x)
