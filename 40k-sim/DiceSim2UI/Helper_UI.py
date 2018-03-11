

def clean_hit_input(hit):
    """

    This function will clean up the hit_like input.
    Will throw exception if it's junk

    Returns
    -------
    hit : int
        A number representing the chance to hit of the attacking unit
    """

    hit = hit.strip("+")
    hit = int(hit)
    return hit
