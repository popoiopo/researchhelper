"""Process network data."""

from .timehandeling import filter_timestamps
import networkx as nx


def nx_network(relations, filter_type: str = "all", **kwargs):
    """Return list in networkX format.

    Parameters
    ----------
    filter_type : str
        Filertype string as from `researchhelper.processdata.timehandeling.filterTimeStamps.
        <https://www.baschatel.nl/researchhelper/researchhelper.processdata.html#module-researchhelper.processdata.timehandeling>`_.`
    **kwargs : dict
        Dictionary with arguments for the filterTimeStamps function.

    Returns
    -------
    graph : nx.Graph
        A networkx graph from the provided relations object based on timestamps.

    """
    return nx.Graph([(d.r_from, d.r_to, {
        "timestamp": d.r_timestamp
    }) for d in filter_timestamps(relations, filter_type, **kwargs)])
