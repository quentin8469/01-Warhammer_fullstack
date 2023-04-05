def list_players_attak_rank(init_player):
    """
    Create a liste with the initiative of all player
    return a list of tuple [(init,[player_name])]
    """
    liste_une = []
    liste_deux = []
    for player in init_player:
        liste_une.append(player.init_list_tuple())
    for trucs in liste_une:
        for truc in trucs:
            liste_deux.append(truc)
    return liste_deux


def dict_players_attak_rank(autre_truc):
    """
    Create a revers ordered dictionnary with the list_players_attak_rank
    return a dictionnary {"init nb" : (list_players_attak_rank),}
    """
    dico_un = {}
    dico_deux = {}
    for k, v in autre_truc:
        dico_un.setdefault(k, []).append(v)
    test = sorted(dico_un.items(), reverse=True)
    for i in range(len(dico_un)):
        dico_deux[f"init {i}"] = test[i]
    return dico_deux


def format_dict_players_attak_rank(dict_attak_rank):
    """
    Format the dict_players_attak_rank to a dictionnary
    return a dictionnary for the template initiative groupe
    """
    dict_for_template = {}
    for k, v in dict_attak_rank.items():
        dict_for_template[v[0]] = v[1]
    return dict_for_template


def get_actual_carriere(plan_carrieres):
    """
    return the actual carriere of the player
    """
    actual_carrriere = []
    for carriere in plan_carrieres:
        actual_carrriere.append(carriere.nom)
    return actual_carrriere
