
def position_dictionary():
    """
    Creates a collection of all position codes, with their associated general position.
    Work in progress.

    Returns:
        dict:Dictionary containing position code strings as keys, and a string representing the general position as
        values.
    """

    pos_dict = dict.fromkeys(['RW', 'LW'], 'Winger')
    pos_dict.update(dict.fromkeys(['GK'], 'Goalkeeper'))
    pos_dict.update(dict.fromkeys(['LB', 'RB', 'LWB', 'RWB'], 'Full Back'))
    pos_dict.update(dict.fromkeys(['CB', 'LCB', 'RCB', 'SW'], 'Center Back'))
    pos_dict.update(dict.fromkeys(['DMF'], 'Defensive Midfielder'))
    pos_dict.update(dict.fromkeys(['AMF'], 'Attacking Midfielder'))
    pos_dict.update(dict.fromkeys(['CMF', 'LCMF', 'RCMF'], 'Center Midfielder'))
    pos_dict.update(dict.fromkeys(['CF', 'LCF', 'RCF'], 'Striker'))
    return pos_dict


def main_position(player, pos_dict):
    """
    Returns the general position corresponding to a player's main position in string form.
    """

    position = player['Main Position']
    return pos_dict.get(position)
