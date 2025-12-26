class Plugin:
    PluginRegistry = {}
    
    def __init_subclass__(cls, /, name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        
        if not name:
            raise ValueError("Плагин должен иметь атрибут 'name'")
        
        if name in Plugin.PluginRegistry:
            raise ValueError(f"Плагин с именем '{name}' уже существует")
        
        Plugin.PluginRegistry[name] = cls
        cls._name = name
    
    def execute(self, data: str) -> str:
        raise NotImplementedError(data)
    
class UpperCasePlugin(Plugin, name="upper"):
    def execute(self, data: str) -> str:
        return data.upper()
    
class ReversePlugin(Plugin, name="reverse"):
    def execute(self, data: str) -> str:
        return data[::-1]

class CapitalizePlugin(Plugin, name="capitalize"):
    def execute(self, data: str) -> str:
        return data.capitalize()