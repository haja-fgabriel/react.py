from react import React


class TestReactCreateComponent:
    def test_ok(self):
        component = React.create_element("div", {}, "Hello World!")
        assert isinstance(component, React.Component)
