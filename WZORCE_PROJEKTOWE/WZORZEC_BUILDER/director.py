from builder import Builder

class Director:
    def __init__(self) -> None:
        self._builder =None
        
    @property
    def builder(self)->None:
        return self._builder
    
    @builder.setter
    def builder(self,builder:Builder) -> None:
        self._builder = builder
        
    def build_minial_version(self) -> None:
        self._builder.produce_part_a()
        
    def build_full_version(self) -> None:
        self._builder.produce_part_a()
        self._builder.produce_part_b()
        self._builder.produce_part_c()
