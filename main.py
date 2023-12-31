def define_env(env):
    @env.macro
    def since(version, mod="minecells"):
        versionId = version.split('-')[-1]
        link = f'https://modrinth.com/mod/{mod}/version/{versionId}/'
        return f'<span class="since">Available since <a target="_blank" href="{link}">{version}</a></span>\n'