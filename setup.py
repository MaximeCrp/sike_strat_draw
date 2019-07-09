from setuptools import setup

setup(
    name="sike_strat_draw",
    version="0.4",
    description="Tool to draw SIKE or other isogeny-based crypotgraphic protocols strategies",
    url="https://github.com/MaximeCrp/sike_strat_draw",
    author="Maxime Crampon",
    author_email="maxime.crampon@protonmail.com",
    packages=["sike_strat_draw"],
    install_requires=["canvasvg", "datetime"],
)
