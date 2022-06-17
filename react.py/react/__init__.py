from abc import abstractmethod


class React:
    class Component:
        def __init__(self, type, props={}) -> None:
            self.props = props
            self.ref = None
            self.type = type
            self.key = None

        @abstractmethod
        def component_did_mount(self):
            pass

    def create_element(element, props={}, children=[]):
        _props = {**props}
        _props["children"] = children
        return React.Component(element, props)
        # renderer =


# class _ReactRendererFactory:
#     def get_renderer_for_element(element):
#         if isinstance(element, str):
#             pass
#         elif isinstance(element, React.Component):
#             pass
#         elif isinstance(element, function):
#             pass

# class _ReactRenderer:
#     pass

# class _ReactStrRenderer:
#     pass

# class _ReactComponentRenderer:
#     pass

# def use_state(initial_value):
#     pass

# def use_effect(effect, dependencies):
#     pass
