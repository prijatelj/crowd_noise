"""
Documentation of desired TTS code, but in python format with desired style
"""
import random
import subprocess
import os

def espeak(text, output_path, name='singleton', pitch=(82, 118), formant=None, echo=None,
    tone=(600,170,1200,135,2000,110), flutter=2, roughness=2, voicing=100, consonants=(100,100),
    breath=None, breathw=None, speed=100, language='en', gender='male',
    output_filetype='.wav'):
    """
    A python wrapper function that interfaces with espeak via CLI. Given text,
    creates an output audio file of voice speaking that text.

    :param text: Text to be spoken by espeak voice
    :param output_path: File path to the desired output, including desired
        filename
    :param output_filetpye: str file extension of file type for output
    :param others: All of the parameters match that of espeak voices. Language
        and gender are optional http://espeak.sourceforge.net/voices.html
    """

    #Create voice

    workingDirectory = os.path.realpath('')
    
    voicesDirectory = os.path.join(workingDirectory, 'espeak-data', 'voices')

    voiceFileName = 'singleton'

    voiceFilePath = os.path.join(voicesDirectory,voiceFileName)

    voiceFile = open(voiceFilePath,'w')

    voiceFile.write('name '+name)

    voiceFile.write('\nlanguage '+language)

    voiceFile.write('\ngender '+gender)

    voiceFile.write('\npitch '+str(pitch[0])+' '+str(pitch[1]))

    #Proper parameter format is a list of lists or [[]]
    if formant is not None:
        for list in formant:
            voiceFile.write('\nformant '+str(list[0])+' '+str(list[1])+' '+str(list[2])+' '+str(list[3]))

    if echo is not None:
        voiceFile.write('\necho '+str(echo[0])+' '+str(echo[1]))

    voiceFile.write('\ntone')
    for item in tone:
       voiceFile.write(' '+str(item))

    voiceFile.write('\nflutter '+str(flutter))

    voiceFile.write('\nroughness '+str(roughness))

    voiceFile.write('\nvoicing '+str(voicing))

    voiceFile.write('\nconsonants '+str(consonants[0])+' '+str(consonants[1]))
    
    if breath is not None:
        voiceFile.write("\nbreath ")
        for item in breath:
            voiceFile.write(' '+str(item))

    if breathw is not None:
        voiceFile.write("\nbreath ")
        for item in breath:
            voiceFile.write(' '+str(item))

    voiceFile.write('\nspeed '+str(speed))

    voiceFile.close()

    #Voice should be written now

    #Build the command to run

    #Command Base
    cmd = 'espeak '
     
    #Set Voice Directory
    cmd += '--path='+workingDirectory+' '

    #Set Voice
    cmd += '-v '+name+' '

    #Set file saving
    cmd += '-w '+output_path+output_filetype+' '

    #Set the text being said
    cmd += text

    #And now we run the command

    print subprocess.check_output(cmd,stderr=subprocess.PIPE).decode('UTF-8'))

    # no return

def random_espeak(text, output_path, name, pitch=(82, 118), formant=None,
    echo=None, tone=None, flutter=2, roughness=2, voicing=100,
    consonants=(100,100), breath=0, breathw=None, speed=100, language=None,
    gender=None, output_filetype='wav'):
    """
    A wrapper of espeak python interface wrapper. This wrapper randomizes the
    parameter inputs given certain ranges and discrete items to select from.

    :param text: Text to be spoken by espeak voice
    :param output_path: File path to the desired output, including desired
        filename
    :param output_filetpye: str file extension of file type for output
    :param others: Ranges or discrete sets to be randomly selected from for all
        of the parameters match that of
        http://espeak.sourceforge.net/voices.html All default values of the
        parameters are to be either set to the limits of each espeak parameter,
        or to reasonable limits from testing that change the voice without
        making it sound too unnatrual.
    """
    # TODO update default params of function. Currently match espeak() defaults.

    # code example:
    # name param should default to a set of default names in espeak
    name = {'name1', 'name2', 'name3'} #this is notation for python set
    pitch = ((0,100), (0,200)) # example of pitch default parameter, fake values

    # can overwrite param vars with random select for readability.
    pitch = (random.randint(pitch[0][0], pitch[0][1]),
        random.randint(pitch[1][0], pitch[1][1]))

    espeak(
        text,
        output_path,
        random.choice(name),
        pitch,
        # fill in rest of espeak params similarly
        output_filetype=output_filetype
    )

    # no return
if __name__ == '__main__':

    #TODO Remove later on. Currently just being used for some unit testing
    espeak('test', '/home/magic/crowdnoise/crowd_noise/results/test')