# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0005)

optimizer_config = dict(grad_clip=None)

# learning policy
lr_config = dict(
    policy='step',
    #warmup='constant',
    warmup=None,
    # warmup_iters=500,
    # warmup_ratio=1,
    # gamma=0.1,
    step=99)

runner = dict(type='EpochBasedRunner', max_epochs=100)
