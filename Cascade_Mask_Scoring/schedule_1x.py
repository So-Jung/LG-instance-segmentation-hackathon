# optimizer
optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001)

optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[8, 11])
runner = dict(type='EpochBasedRunner', max_epochs=12)

# # PyTorch에서 제공하는 optimizer 
# # SGD 
# optimizer = dict(type='SGD', lr=<required parameter>, momentum=0, dampening=0, weight_decay=0, nesterov=False, maximize=False, foreach=None)
# # ASGD
# optimizer = dict(type='ASGD',lr=0.01, lambd=0.0001, alpha=0.75, t0=1000000.0, weight_decay=0, foreach=None)
# # Adadelta
# optimizer = dict(type='Adadelta', lr=1.0, rho=0.9, eps=1e-06, weight_decay=0, foreach=None, maximize=False)
# # Adam
# optimizer = dict(type='Adam',lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, amsgrad=False, foreach=None, maximize=False, capturable=False)
# # AdamW
# optimizer = dict(type='AdamW', lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0.01, amsgrad=False, maximize=False, foreach=None, capturable=False)
# # Nadam
# optimizer = dict(type='Nadam', lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004, foreach=None)
# # Radam
# optimizer = dict(type='Radam', lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, foreach=None)
# # Adagrad
# optimizer = dict(type='Adagrad', lr=0.01, lr_decay=0, weight_decay=0, initial_accumulator_value=0, eps=1e-10, foreach=None, maximize=False)
# # Adamax
# optimizer = dict(type='Adamax', lr=0.002, betas=(0.9,0.999), eps=1e-08, weight_decay=0, foreach=None, maximize=False)
# # RMSprop
# optimizer = dict(type='RMSprop', lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False, foreach=None)
