
"""

eSpeak wrapper and interface for Python

@author Matthew "SpudManTwo" Kaufman

"""
import random
import subprocess
import os

def espeak(text, output_path, name='temp', pitch=(82, 118), formant=None, 
    echo=None, tone=(600,170,1200,135,2000,110), flutter=2, roughness=2, voicing=100, consonants=(100,100),
    breath=None, breathw=None, speed=100, language='en', gender='male'):
    """

    Speaks given text into a file, using either the default voice parameters or custom voice options given.

    @params

        @required
            text (String): Text to be spoken by espeak voice
            
            output_path (Path to Directory as String): File path to the desired output.
    
        @optional

            workingDirectory (Path as String): Path to where the espeak-data is stored.
                Defaults to where this source code is being held.

            voicesDirectory (Path as String): Path to where voices are stored.
                Defaults to a path relative to workingDirectory.

            name (String): Name of the voice/voice file. 
                Defaults to "temp"
    
            pitch (Range): Pitch Range used for the voice being created. 
                Default is eSpeak Default.
            
            formant (List< List<Integer> of size 5 > up to size 8 ): List of the different formant data for the voice. Order in the list is, 
                { formant Number , frequency , strength, width, constant value added to the frequency when in formant peak. }
    
            echo ( List <Integer> ) : List of parameters being used for the custom voice. Order in the list is, 
                { delay in milliseconds, echo amplitude }

            tone ( List <Integer>  up to size 8) : List of up to 4 pairs that changes the frequency and amplitudes for the 
                frequency response graph. 
                Default is eSpeak default.

            flutter (Integer) : Adds pitch fluctuations to the custom voice to give a wavering or older sounding voice. 
                Default is eSpeak default

            roughness (Integer in the range of 0 -7) : Reduces the amplitude of alternate waveform cycles. 
                Makes the voice sound more or less 'creaky'. 
                Default is eSpeak default.

            voicing (Integer) : Changes the strength of the formant-synthesized sounds. 
                Default is eSpeak default.

            consonants ( (Integer , Integer) ): Adjusts the srength of noise sounds used in Consonants.
                The first value controls 'unvoiced consonants' like 's' and 't'. 
                The second controls the strength of 'voiced' consonants like 'v' and 'd'.

            breath ( List<Integer> up to size 8) : List of integers that adds noise which corresponds to formant frequency peaks. 
                Each value corresponds to the corresponding formant value. 
                When used in combination with a low or zero voicing attribute, makes it sound like a whisper.
                {formant 1 noise addition, formant 2 noise addition, ... , formant 8 noise addition }

            breathw ( List<Integer> up to size 8 ) : List of bandwiths of the noise peaks that correspond with breath attribute/s.
                Defaults to a suitable value

            speed (Integer) : Adjusts the speaking speed by a percentage of the default rate.
                Default is eSpeak Default.

            language (ISO 639-1 language code as String) : Selects and sets all the default behaviors for the language.

            gender ( String ): Has no real functional application. Just used for voice selection
                Defaults to 'male'.

    @returns

        no return

    @output

        Creates a new .wav file of the text being spoken using the specified voice parameters at the specified location 

        Creates a new voice file using either default parameters or given parameters.

    """

    #Initialize the directories if they aren't already

    workingDirectory = os.path.dirname(os.path.realpath(''))

    dataDirectory = os.path.join(workingDirectory,'data')

    voicesDirectory = os.path.join(dataDirectory, 'espeak-data', 'voices')


    #Create voice

    makeVoice(voicesDirectory,name,pitch,formant,echo,tone,flutter,roughness,voicing,consonants,breath,breathw,speed,language,gender)

    #Voice should be written now

    #Say using our new fancy custom voice.

    say(text,output_path,name,dataDirectory)

    # no return

def makeVoice(voicesDirectory, name='temp', pitch=(82, 118), formant=None, echo=None,
    tone=(600,170,1200,135,2000,110), flutter=2, roughness=2, voicing=100, consonants=(100,100),
    breath=None, breathw=None, speed=100, language='en', gender='male'):

    """

    Creates a new voice using given parameters

    @params

        @required

            voicesDirectory (Path as String): Path to the directory where the eSpeak voices are being stored.

        @optional
            name (String): Name of the voice/voice file. 
                Defaults to "temp"
    
            pitch (Range): Pitch Range used for the voice being created. 
                Default is eSpeak Default.
            
            formant (List< List<Integer> of size 5 > up to size 8 ): List of the different formant data for the voice. Order in the list is, 
                { formant Number , frequency , strength, width, constant value added to the frequency when in formant peak. }
    
            echo ( List <Integer> ) : List of parameters being used for the custom voice. Order in the list is, 
                { delay in milliseconds, echo amplitude }

            tone ( List <Integer>  up to size 8) : List of up to 4 pairs that changes the frequency and amplitudes for the 
                frequency response graph. 
                Default is eSpeak default.

            flutter (Integer) : Adds pitch fluctuations to the custom voice to give a wavering or older sounding voice. 
                Default is eSpeak default

            roughness (Integer in the range of 0 -7) : Reduces the amplitude of alternate waveform cycles. 
                Makes the voice sound more or less 'creaky'. 
                Default is eSpeak default.

            voicing (Integer) : Changes the strength of the formant-synthesized sounds. 
                Default is eSpeak default.

            consonants ( (Integer , Integer) ): Adjusts the srength of noise sounds used in Consonants.
                The first value controls 'unvoiced consonants' like 's' and 't'. 
                The second controls the strength of 'voiced' consonants like 'v' and 'd'.

            breath ( List<Integer> up to size 8) : List of integers that adds noise which corresponds to formant frequency peaks. 
                Each value corresponds to the corresponding formant value. 
                When used in combination with a low or zero voicing attribute, makes it sound like a whisper.
                {formant 1 noise addition, formant 2 noise addition, ... , formant 8 noise addition }

            breathw ( List<Integer> up to size 8 ) : List of bandwiths of the noise peaks that correspond with breath attribute/s.
                Defaults to a suitable value

            speed (Integer) : Adjusts the speaking speed by a percentage of the default rate.
                Default is eSpeak Default.

            language (ISO 639-1 language code as String) : Selects and sets all the default behaviors for the language.

            gender ( String ): Has no real functional application. Just used for voice selection
                Defaults to 'male'.

    @returns

        No return

    @output

        Creates a new voice file using either default parameters or given parameters.
    
    """

    voiceFilePath = os.path.join(voicesDirectory,name)

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

    #no return

def say(text, output_path, name, dataDirectory):

    """

    Speaks given text using the specified voice name and outputs result as .wav file in specified path.

    @params

        @required
            text (String): Text to be spoken by espeak voice
            
            output_path (Path to Directory as String): File path to the desired output.

            name (String): Name of voice being used to speak text.

            dataDirectory (Path as String): Path to the directory that contains the espeak-data.

    @returns

        No return

    @output

        Outputs a .wav audio file at specified location of spoken text using specified voice.
    
    """

    #Build the command to run

    #Command Base
    cmd = ['espeak']
     
    #Set Voice Directory
    cmd = cmd + ['--path='+dataDirectory]

    #Set Voice

    cmd = cmd  + ['-v'+name]

    #Set file saving
    cmd =  cmd + ['-w '+output_path+'.wav']

    #Set the text being said
    cmd = cmd + ['\"'+text+'\"']

    #And now we run the command

    subprocess.call(cmd)

    #no return

def random_espeak(text, output_path,  name = ('name1', 'name2', 'name3'),  pitch = ((60,100),(82,118),(120,160)), formant=(None,None,None),
    echo=(None,None,None), tone=((600,170,1200,135,2000,110),(600,170,1200,135,2000,110),(600,170,1200,135,2000,110)), flutter=(1,2,3), roughness=(1,2,3), voicing=(100,100,100),
    consonants=((100,100),(100,100),(100,100)), breath=(None,None,None), breathw=(None,None,None), speed=(75,100,125), language=('en','en','en'),
    gender=('male','male','female')):
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

    #Select the Index that we're gonna roll with
    selectedIndex = random.randint(0,len(name))

    print(selectedIndex)

    # can overwrite param vars with random select for readability.
    # pitch = (random.randint(pitch[0][0], pitch[0][1]),random.randint(pitch[1][0], pitch[1][1]),random.randint(pitch[2][0], pitch[2][1]))
    # TODO: Maybe later if people want it? Wouldn't be hard... - Matt

    espeak(
        text,
        output_path,
        name[selectedIndex],
        pitch[selectedIndex],
        formant[selectedIndex],
        echo[selectedIndex],
        tone[selectedIndex], 
        flutter[selectedIndex],
        roughness[selectedIndex],
        voicing[selectedIndex],
        consonants[selectedIndex],
        breath[selectedIndex],
        breathw[selectedIndex],
        speed[selectedIndex],
        language[selectedIndex],
        gender[selectedIndex]
    )

    # no return