

class IIdentifiable:
    _recent_id = -1

    def _assign_id(self):
        IIdentifiable._recent_id += 1
        return IIdentifiable._recent_id

