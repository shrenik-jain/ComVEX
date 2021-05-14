class SwinTransformerConfig(object):
    def __init__(
        self, 
        *,
        image_channel, 
        image_size, 
        patch_size,
        num_channels,
        num_layers_in_stages, 
        head_dim,
        window_size,
        shifts,
        num_classes,
        use_absolute_position,
        use_checkpoint,
        use_pre_norm=False, 
        ff_dim=None, 
        ff_dropout=0.0,
        attention_dropout=0.0,
        token_dropout=0.0,
    ) -> None:

        self.image_channel =image_channel 
        self.image_size = image_size 
        self.patch_size = patch_size
        self.num_channels = num_channels
        self.num_layers_in_stages = num_layers_in_stages 
        self.head_dim = head_dim
        self.window_size = window_size
        self.shifts = shifts
        self.num_classes = num_classes
        self.use_absolute_position = use_absolute_position
        self.use_checkpoint = use_checkpoint
        self.use_pre_norm = use_pre_norm 
        self.ff_dim = ff_dim 
        self.ff_dropout = ff_dropout
        self.attention_dropout = attention_dropout
        self.token_dropout = token_dropout

    @classmethod
    def SwinTransformer_T(
        cls, 
        image_channel: int,
        image_size: int,
        num_classes: int, 
        use_absolute_position: bool,
        use_checkpoint: bool,
        use_pre_norm: bool = False, 
        ff_dropout: float = 0.0,
        attention_dropout: float = 0.0,
        token_dropout: float = 0.0,
    ) -> "SwinTransformerConfig":
        return cls(
            image_channel=image_channel, 
            image_size=image_size, 
            patch_size=4,
            num_channels=96,
            num_layers_in_stages=[2, 2, 6, 2], 
            head_dim=32,
            window_size=(7, 7),
            shifts=2,
            num_classes=num_classes,
            use_absolute_position=use_absolute_position,
            use_checkpoint=use_checkpoint,
            use_pre_norm=use_pre_norm, 
            ff_dropout=ff_dropout,
            attention_dropout=attention_dropout,
            token_dropout=token_dropout,
        )

    @classmethod
    def SwinTransformer_S(
        cls, 
        image_channel: int, 
        image_size: int, 
        num_classes: int, 
        use_absolute_position: bool,
        use_checkpoint: bool,
        use_pre_norm: bool = False, 
        ff_dropout: float = 0.0,
        attention_dropout: float = 0.0,
        token_dropout: float = 0.0,
    ) -> "SwinTransformerConfig":
        return cls(
            image_channel=image_channel, 
            image_size=image_size, 
            patch_size=4,
            num_channels=96,
            num_layers_in_stages=[2, 2, 18, 2], 
            head_dim=32,
            window_size=(7, 7),
            shifts=2,
            num_classes=num_classes,
            use_absolute_position=use_absolute_position,
            use_checkpoint=use_checkpoint,
            use_pre_norm=use_pre_norm, 
            ff_dropout=ff_dropout,
            attention_dropout=attention_dropout,
            token_dropout=token_dropout,
        )
    
    @classmethod
    def SwinTransformer_B(
        cls, 
        image_channel: int, 
        image_size: int, 
        num_classes: int, 
        use_absolute_position: bool,
        use_checkpoint: bool,
        use_pre_norm: bool = False, 
        ff_dropout: float = 0.0,
        attention_dropout: float = 0.0,
        token_dropout: float = 0.0,
    ) -> "SwinTransformerConfig":
        return cls(
            image_channel=image_channel, 
            image_size=image_size, 
            patch_size=4,
            num_channels=128,
            num_layers_in_stages=[2, 2, 18, 2], 
            head_dim=32,
            window_size=(7, 7),
            shifts=2,
            num_classes=num_classes,
            use_absolute_position=use_absolute_position,
            use_checkpoint=use_checkpoint,
            use_pre_norm=use_pre_norm, 
            ff_dropout=ff_dropout,
            attention_dropout=attention_dropout,
            token_dropout=token_dropout,
        )

    @classmethod
    def SwinTransformer_L(
        cls, 
        image_channel: int, 
        image_size: int, 
        num_classes: int, 
        use_absolute_position: bool,
        use_checkpoint: bool,
        use_pre_norm: bool = False, 
        ff_dropout: float = 0.0,
        attention_dropout: float = 0.0,
        token_dropout: float = 0.0,
    ) -> "SwinTransformerConfig":
        return cls(
            image_channel=image_channel, 
            image_size=image_size, 
            patch_size=4,
            num_channels=192,
            num_layers_in_stages=[2, 2, 18, 2], 
            head_dim=32,
            window_size=(7, 7),
            shifts=2,
            num_classes=num_classes,
            use_absolute_position=use_absolute_position,
            use_checkpoint=use_checkpoint,
            use_pre_norm=use_pre_norm, 
            ff_dropout=ff_dropout,
            attention_dropout=attention_dropout,
            token_dropout=token_dropout,
        )