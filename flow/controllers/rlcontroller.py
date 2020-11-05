"""Contains the RLController class."""

from flow.controllers.base_controller import BaseController


class RLController(BaseController):
    """RL Controller.

    Vehicles with this class specified will be stored in the list of the RL IDs
    in the Vehicles class.

    Usage: See base class for usage example.

    Attributes
    ----------
    veh_id : str
        Vehicle ID for SUMO identification

    Examples
    --------
    A set of vehicles can be instantiated as RL vehicles as follows:

        >>> from flow.core.params import VehicleParams
        >>> vehicles = VehicleParams()
        >>> vehicles.add(acceleration_controller=(RLController, {}))

    In order to collect the list of all RL vehicles in the next, run:

        >>> from flow.envs import Env
        >>> env = Env(...)
        >>> rl_ids = env.k.vehicle.get_rl_ids()
    """

    def __init__(self, veh_id, car_following_params):
        """Instantiate an RL Controller."""
        BaseController.__init__(
            self,
            veh_id,
            car_following_params)

    def get_accel(self, env):
        """Pass, as this is never called; required to override abstractmethod."""
        pass


"""Contains a list of custom lane change controllers."""

from flow.controllers.base_lane_changing_controller import \
    BaseLaneChangeController


class lanechange_RLcontroller(BaseLaneChangeController):
    """A controller used to enforce sumo lane-change dynamics on a vehicle.

    Usage: See base class for usage example.
    """
    def __init__(self,veh_id,lane_change_params=None):
        BaseLaneChangeController.__init__(self, veh_id,lane_change_params)

    def get_lane_change_action(self, env):
        """See parent class."""
        # TODO : change direction from 0,1,2 to -1,0,1
        return 0

    def get_action(self, env):
        """Return the action of the lane change controller.

        Modifies the lane change action to ensure safety, if requested.

        Parameters
        ----------
        env : flow.envs.Env
            state of the environment at the current time step

        Returns
        -------
        float or int
            lane change action
        """
        lc_action = self.get_lane_change_action(env)
        return lc_action
