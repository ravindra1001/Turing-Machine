import cx_Freeze

executables=[cx_Freeze.Executable("mainfile.py")]

cx_Freeze.setup(
    name="Turing_Machine",
    options={"build_exe":{"packages":["pygame"],"include_files":["ravindra.png","shrey.png","krc.png"]}},
    description="this is a turing machine",
    executables=executables
    )
