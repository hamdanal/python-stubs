def read_pm_results_to_net(net, ppc, ppci, result_pm) -> None: ...
def add_storage_results(net, result_pmi) -> None: ...
def add_time_series_data_to_net(net, controller, tp) -> None: ...
def pm_results_to_ppc_results(net, ppc, ppci, result_pm): ...
def pm_results_to_ppc_results_one_time_step(ppci, sol) -> None: ...
def read_ots_results(net) -> None: ...
def read_tnep_results(net) -> None: ...
