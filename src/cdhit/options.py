class Options:
    opt = {
        "backupFile": False,
        "useIdentity": False,
        "useDistance": False,
        "has2D": False,
        "isEST": False,
        "is454": False,
        "NAA": 5,
        "NAA_top_limit": 5,
        "cluster_thd": 0.9,
        "distance_thd": 0.0,
        "max_memory": 800000000,
        "min_length": 10,
        "cluster_best": False,
        "global_identity": True,
        "store_disk": False,
        "band_width": 20,
        "diff_cutoff": 0.0,
        "diff_cutoff2": 1.0,
        "diff_cutoff_aa": 99999999,
        "diff_cutoff_aa2": 0,
        "tolerance": 2,
        "long_coverage": 0.0,
        "long_control": 99999999,
        "short_coverage": 0.0,
        "short_control": 99999999,
        "long_unmatch_per": 1.0,
        "short_unmatch_per": 1.0,
        "unmatch_len": 99999999,
        "min_control": 0,
        "max_indel": 1,
        "print_out": 0,
        "option_r": 1,
        "frag_size": 0,
        "des_len": 20,
        "threads": 1,
        "PE_mode": 0,
        "trim_len": 0,
        "trim_len_R2": 0,
        "align_pos": 0,
        "sort_output": 0,
        "sort_outputf": 0,
        "max_entries": 0,
        "max_sequences": 1 << 20,
        "mem_limit": 100000000,
    }

    def set_option_common(self, flag, value):
        pass

    def set_option(self, flag, value):
        pass

    def set_option_2d(self, flag, value):
        pass

    def set_option_est(self, flag, value):
        pass

    def set_options(self, argc, argv, two_data: bool = False, est: bool = False):
        pass

    def validate(self):
        pass

    def compute_table_limits(self, min_len: int, max_len: int, typical_len: int, mem_need: int):
        pass

    def print_options(self):
        print(f"isEST = {self.opt['isEST']}\n")
        print(f"has2D = {self.opt['has2D']}\n")
        print(f"NAA = {self.opt['NAA']}\n")
        print(f"NAA_top_limit = {self.opt['NAA_top_limit']}\n")
        print(f"min_length = {self.opt['min_length']}\n")
        print(f"cluster_best = {self.opt['cluster_best']}\n")
        print(f"global_identity = {self.opt['global_identity']}\n")
        print(f"cluster_thd = {self.opt['cluster_thd']}\n")
        print(f"diff_cutoff = {self.opt['diff_cutoff']}\n")
        print(f"diff_cutoff_aa = {self.opt['diff_cutoff_aa']}\n")
        print(f"tolerance = {self.opt['tolerance']}\n")
        print(f"long_coverage = {self.opt['long_coverage']}\n")
        print(f"long_control = {self.opt['long_control']}\n")
        print(f"short_coverage = {self.opt['short_coverage']}\n")
        print(f"short_control = {self.opt['short_control']}\n")
        print(f"frag_size = {self.opt['frag_size']}\n")
        print(f"option_r = {self.opt['option_r']}\n")
        print(f"print = {self.opt['print_out']}\n")
