from keras import Input
from keras.engine import Layer, Model
from keras.layers import Activation, BatchNormalization, Convolution2D, Dense, Flatten, MaxPooling2D, AveragePooling2D, \
    add
from keras.models import Sequential
from keras.regularizers import l2
from keras.utils import plot_model

from models.TrainingConfiguration import TrainingConfiguration


class ResNet5Configuration(TrainingConfiguration):
    """ A network with residual modules """

    def __init__(self, optimizer="Adadelta", width=24, height=24, training_minibatch_size=64):
        super().__init__(optimizer=optimizer, data_shape=(height, width, 3),
                         training_minibatch_size=training_minibatch_size)

    def classifier(self) -> Sequential:
        """ Returns the classifier of this configuration """

        input = Input(shape=self.data_shape)

        layer = self.add_convolution(input, 32, 3)
        layer = self.add_res_net_block(layer, 32, 3, False)
        layer = MaxPooling2D()(layer)

        layer = self.add_res_net_block(layer, 64, 3, True)
        layer = self.add_res_net_block(layer, 64, 3, False)
        layer = MaxPooling2D()(layer)

        layer = self.add_res_net_block(layer, 128, 3, True)
        layer = self.add_res_net_block(layer, 128, 3, False)
        layer = self.add_res_net_block(layer, 128, 3, False)
        layer = MaxPooling2D()(layer)

        layer = self.add_res_net_block(layer, 256, 3, True)
        layer = self.add_res_net_block(layer, 256, 3, False)
        layer = self.add_res_net_block(layer, 256, 3, False)
        # layer = MaxPooling2D()(layer)
        #
        # layer = self.add_res_net_block(layer, 512, 3, True)
        # layer = self.add_res_net_block(layer, 512, 3, False)
        # layer = self.add_res_net_block(layer, 512, 3, False)
        layer = AveragePooling2D()(layer)

        feature_vector = Flatten()(layer)

        number_of_output_classes = 32
        classification_head = Dense(units=number_of_output_classes, kernel_regularizer=l2(self.weight_decay),
                                    activation='softmax', name='output_class')(feature_vector)

        classifier = Model(inputs=[input], outputs=[classification_head])
        classifier.compile(self.get_optimizer(),
                           loss={'output_class': 'categorical_crossentropy'},
                           metrics=["accuracy"])
        return classifier

    def add_convolution(self, previous_layer: Layer, filters: int, kernel_size: int):
        layer = Convolution2D(filters, kernel_size, padding='same', kernel_regularizer=l2(self.weight_decay))(
            previous_layer)
        layer = BatchNormalization()(layer)
        layer = Activation('relu')(layer)

        return layer

    def add_res_net_block(self, previous_layer: Layer, filters, kernel_size, shortcut_is_conv) -> Layer:
        layer = BatchNormalization()(previous_layer)
        layer = Activation('relu')(layer)
        layer = Convolution2D(filters, kernel_size, padding='same', kernel_regularizer=l2(self.weight_decay))(layer)
        layer = BatchNormalization()(layer)
        layer = Activation('relu')(layer)
        layer = Convolution2D(filters, kernel_size, padding='same', kernel_regularizer=l2(self.weight_decay))(layer)

        shortcut = previous_layer
        if shortcut_is_conv:
            shortcut = Convolution2D(filters, kernel_size, padding='same', kernel_regularizer=l2(self.weight_decay))(
                previous_layer)

        layer = add([layer, shortcut])

        return layer

    def name(self) -> str:
        """ Returns the name of this configuration """
        return "res_net_5_reduced"

    def performs_localization(self) -> bool:
        return False


if __name__ == "__main__":
    configuration = ResNet5Configuration()
    classifier = configuration.classifier()
    classifier.summary()
    plot_model(classifier, to_file="res_net_5.png")
    print(configuration.summary())
