class MassWastingSaver:
    """This class is instantiated and called by MassWastingRunout. It saves
    MWR model output. It is only called in MassWastingRunout if save = True"""

    def __init__(self, MassWastingRunout):
        self.MWR = MassWastingRunout

    def prep_data_containers(self):
        # lists and dictionaries for tracking model behavior
        self.runout_evo_maps = {}  # runout material + topographic__elevation


    def prep_mw_data_containers(self, mw_i, mw_id):
        # containeers for each unique mass wasting ID
        self.runout_evo_maps[mw_i] = {}


    def save_conditions_before_runout(self, mw_i, mw_id):
        # save first set of data to reflect scar/depression in DEM created by
        # mass wasting source area
        self.runout_evo_maps[mw_i][0] = self.MWR._grid.at_node[
            "energy__elevation"
        ].copy()


    def save_conditions_after_one_iteration(self, mw_i, mw_id):

        self.runout_evo_maps[mw_i][self.MWR.c + 1] = self.MWR._grid.at_node[
            "energy__elevation"
        ].copy()


    def save_flow_stats(self, E, A, qsi, slpn, Tau, u):
        pass

