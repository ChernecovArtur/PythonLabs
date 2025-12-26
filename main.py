from plugin import Plugin

if __name__ == "__main__":
    print("Реестр плагинов:")
    print(Plugin.PluginRegistry)
    
    test_string = "test string"
    print(f"\nТестовая строка: '{test_string}'")
    
    for plugin_name in Plugin.PluginRegistry:
        plugin_class = Plugin.PluginRegistry[plugin_name]
        plugin_instance = plugin_class()
        result = plugin_instance.execute(test_string)
        print(f"{plugin_name}: '{result}'")
     