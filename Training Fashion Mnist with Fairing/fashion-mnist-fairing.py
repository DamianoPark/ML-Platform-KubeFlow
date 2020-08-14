#!/usr/bin/env python
# coding: utf-8

# # fashion mnist

# In[2]:


import tensorflow as tf
import os


class MyFashionMnist(object):
    def train(self):
        (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        model = tf.keras.models.Sequential([
          tf.keras.layers.Flatten(input_shape=(28, 28)),
          tf.keras.layers.Dense(128, activation='relu'),
          tf.keras.layers.Dropout(0.2),
          tf.keras.layers.Dense(10, activation='softmax')
        ])
        model.summary()
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=10)

        model.evaluate(x_test,  y_test, verbose=2)

if __name__ == '__main__':
    if os.getenv('FAIRING_RUNTIME', None) is None:
        from kubeflow import fairing
        from kubeflow.fairing.kubernetes import utils as k8s_utils

        DOCKER_REGISTRY = 'jaewoo201'
        fairing.config.set_builder(
            'append',
            base_image='jaewoo201/kubeflow-jupyter-lab:tf2.0-cpu',
            registry=DOCKER_REGISTRY, 
            push=True)
        # cpu 2, memory 5GiB
        fairing.config.set_deployer('job',
                                    pod_spec_mutators=[
                                        k8s_utils.get_resource_mutator(cpu=1,
                                                                       memory=2)]
         
                                   )
        fairing.config.run()
    else:
        remote_train = MyFashionMnist()
        remote_train.train()


# In[ ]:




