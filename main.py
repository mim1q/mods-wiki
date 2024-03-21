import textwrap
import re

def id_str(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9 -]', '', name.lower()).replace(' ', '-')

def define_env(env):
    @env.macro
    def since(version, mod="minecells"):
        versionId = version.split('-')[-1]
        link = f'https://modrinth.com/mod/{mod}/version/{versionId}/'
        return f'<span class="since">Available since <a target="_blank" href="{link}">{version}</a></span>\n'

    @env.macro
    def minecells_mob(
        name: str, 
        description: str, 
        biomes: list[str], 
        drops: list[(str, str)] = [], 
        since_version: str = None
    ):
        biomes = '\n'.join([f'- [{biome}](./dimensions.md#{id_str(biome)})' for biome in biomes])
        drops_info = ''
        if len(drops) > 0:
            drops_info += "/// info | Drops\n"

            for drop in drops:
                drops_info += f' - [{drop[0]}](./{drop[1]}.md#{id_str(drop[0])})\n' if drop[1] else f' - {drop[0]}\n'
                
            drops_info += "\n///"

        result = f"""
        ## {name}

        {since(since_version) if since_version is not None else ''}

        ![{name}](img/mobs/{id_str(name)}.jpg){{: .side-image }}

        {' '.join(description.split())}

        /// info | Spawns in
        {biomes}
        ///

        {drops_info}
        
        """

        return '\n'.join([line.strip() for line in textwrap.dedent(result).split('\n')])