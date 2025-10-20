from typing import Any, Callable, cast

from pandas import DataFrame, json_normalize

from impresso.api_client.api.experiments import (
    interact_with_experiment,
    find_experiments,
)
from impresso.api_client.models.find_experiments_base_find_response import (
    FindExperimentsBaseFindResponse,
)
from impresso.api_client.models.freeform import Freeform
from impresso.api_client.models.interact_with_experiment_body import (
    InteractWithExperimentBody,
)
from impresso.data_container import DataContainer
from impresso.resources.base import Resource
from impresso.util.error import raise_for_error

from impresso.api_models import BaseFind, ExperimentInfo


class FindExperimentsSchema(BaseFind):
    """Schema for the find experiments response."""

    data: list[ExperimentInfo]


class FindExperimentsContainer(DataContainer):
    """Response of a find call."""

    def __init__(
        self,
        data: FindExperimentsBaseFindResponse,
        pydantic_model: type[FindExperimentsSchema],
        fetch_method: Callable[..., "FindExperimentsContainer"],
        fetch_method_args: dict[str, Any],
        web_app_search_result_url: str | None = None,
    ):
        super().__init__(data, pydantic_model, web_app_search_result_url)
        self._fetch_method = fetch_method
        self._fetch_method_args = fetch_method_args

    @property
    def df(self) -> DataFrame:
        """Return the data as a pandas dataframe."""
        data = self._data.to_dict()["data"]
        if len(data):
            return json_normalize(self._data.to_dict()["data"]).set_index("id")
        return DataFrame()


class ExperimentsResource(Resource):
    """Experiment with Impresso."""

    name = "experiments"

    def find(self) -> FindExperimentsContainer:
        """Find all available experiments.

        Returns:
            dict: List of available experiments.
        """
        result = find_experiments.sync(
            client=self._api_client,
        )
        raise_for_error(result)

        return FindExperimentsContainer(
            cast(FindExperimentsBaseFindResponse, result),
            FindExperimentsSchema,
            fetch_method=self.find,
            fetch_method_args={},
        )

    def execute(self, experiment_id: str, body: dict) -> dict:
        """Execute an experiment with the given ID.

        Args:
            experiment_id (str): ID of the experiment to execute.
            body (dict): Body of the experiment.

        Returns:
            dict: Result of the experiment.
        """
        result = interact_with_experiment.sync(
            client=self._api_client,
            id=experiment_id,
            body=InteractWithExperimentBody.from_dict(body),
        )
        raise_for_error(result)
        return cast(Freeform, result).to_dict()
