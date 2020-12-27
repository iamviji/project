def Hello(arg):
    print ("Utility", arg)

def get_onehot_ber_bler_of_model (snr_list, encoder, decoder, input_onehot, input_size, channel_size, verbose=1):
    print ("get_onehot_ber_bler_of_model")
    bler_per_iter_dl_tensor  = numpy.array(())
    encoded_message = encoder.predict (input_onehot)
    for snr in snr_list:
        total_bit_error = 0
        total_msg_error = 0
        sigma = ConvSnr2Sigma (snr)
        noised_message = encoded_message + numpy.random.normal(0, sigma, encoded_message.shape)
        for i in range (input_size):
            noised_message[i] = encoded_message[i] + numpy.random.normal(0, sigma, [1,2*channel_size])
        decoded_message = decoder.predict(noised_message)
        for i in range (input_size):
            if (numpy.argmax(input_onehot[i]) != numpy.argmax(decoded_message[i])):
                total_msg_error = total_msg_error + 1
        bler = float(total_msg_error)/input_size
        print('SNR: {:04.3f}:\n -> BER: {:03.2f}'.format(snr,bler))
        bler_per_iter_dl_tensor = numpy.append(bler_per_iter_dl_tensor, bler)
    return bler_per_iter_dl_tensor

def get1_onehot_ber_bler_of_model (snr_list, encoder, decoder, input_onehot, input_size, channel_size, verbose=1):
    print ("get_onehot_ber_bler_of_model")
    bler_per_iter_dl_tensor  = numpy.array(())
    encoded_message = encoder.predict (input_onehot)
    for snr in snr_list:
        total_bit_error = 0
        total_msg_error = 0
        sigma = ConvSnr2Sigma (snr)
        noised_message = encoded_message + numpy.random.normal(0, sigma, encoded_message.shape)
        for i in range (input_size):
            noised_message[i] = encoded_message[i] + numpy.random.normal(0, sigma, [1,2*channel_size])
        decoded_message = decoder.predict(noised_message)
        for i in range (input_size):
            if (numpy.argmax(input_onehot[i]) != numpy.argmax(decoded_message[i])):
                total_msg_error = total_msg_error + 1
        bler = float(total_msg_error)/input_size
        print('SNR: {:04.3f}:\n -> BER: {:03.2f}'.format(snr,bler))
        bler_per_iter_dl_tensor = numpy.append(bler_per_iter_dl_tensor, bler)
    return bler_per_iter_dl_tensor
