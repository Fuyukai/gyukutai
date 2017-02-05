import typing
import types
import collections
# If you ever see this in a project, run.
# This is never a good thing.
import forbiddenfruit


class _Base(object):
    def __init__(self, seq: typing.Sequence):
        self.seq = seq


# `list.find | callable` impl
# This adds a new method to list objects, called `find`
class _FindOr(_Base):
    """
    An or that exports the `.find` method on lists.
    """

    def __or__(self, other: typing.Callable[[typing.Any], bool]):
        if not callable(other):
            cbl = lambda x: x == other
        else:
            cbl = other

        for i in self.seq:
            if cbl(i) is True:
                return i

        return None


find_prop = property(fget=lambda l: _FindOr(l), doc="Given a piped callable, finds an object in the list.")


# `list.apply | callable` impl
class _ApplyOr(_Base):
    def __or__(self, other):
        if not callable(other):
            return NotImplemented

        result = []
        for item in self.seq:
            result.append(other(item))

        return result


apply_prop = property(fget=lambda l: _ApplyOr(l), doc="Given a piped callable, applies it to all items in the list.")


# `list.all | callable` impl
class _AllOr(_Base):
    def __or__(self, other):
        if not callable(other):
            return NotImplemented

        for item in self.seq:
            if other(item) is not True:
                return False

        return True


all_prop = property(fget=lambda l: _AllOr(l),
                    doc="Given a piped callable, ensures all items return True when provided as an argument "
                        "to the callable.")


# `list.any | callable` impl
class _AnyOr(_Base):
    def __or__(self, other):
        if not callable(other):
            return NotImplemented

        for item in self.seq:
            if other(item) is True:
                return True

        return False


any_prop = property(fget=lambda l: _AnyOr(l),
                    doc="Given a piped callable, ensures that at least one item matches.")


# `list.filter | callable` impl
class _FilterOr(_Base):
    def __or__(self, other):
        if not callable(other):
            return NotImplemented

        results = []
        for item in self.seq:
            if other(item) is True:
                results.append(item)

        return results

filter_prop = property(fget=lambda l: _FilterOr(l),
                       doc="Given a piped callable, filters through all items and returns a new sequence.")


def apply():
    """
    Applies the tweaks to the objectss.
    """
    for victim in [list, tuple, collections.Iterable, type({}.keys()), type({}.values())]:
        forbiddenfruit.curse(victim, "find", find_prop)
        forbiddenfruit.curse(victim, "apply", apply_prop)
        forbiddenfruit.curse(victim, "all", all_prop)
        forbiddenfruit.curse(victim, "any", any_prop)
        forbiddenfruit.curse(victim, "filter", filter_prop)
