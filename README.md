# Computational notebooks and experimental manuals for the teaching of electrophisiology

During the last 6 months, I have been working with Dr. Erin McKiernan on the elaboration of code manuals in Python intending to be used for teaching the analysis of electrophysiological signals. 4 sets of manuals were made:

• Electrocardiogram (ECG) analysis manual with data from patients with arrhythmia.

• Electromyogram (EMG) analysis manual with activation data in pulses and fatigue in both hands.

• Manual analysis of spirometry with EMG of the abdomen during a breathing protocol with inspiration, forced inspiration, expiration, and forced expiration.

• Electroencephalogram (EEG) analysis manual for pediatric patients with epilepsy.

All manuals can be found in a public GitHub repository (https://github.com/Javi-ciencias/Servicio_social).

For the first manual, freely accessible data was imported from a database on physionet (https://physionet.org/content/mitdb/1.0.0/). First, a "notebook" was developed that detected P, Q, R, S, and T waves using Fourier transforms and critical point evaluation algorithms. From these markers, he calculated important parameters such as the length of the QRS complex, heart rate, and the length of the P and T waves. The data was fed into a convolutional neural network that was trained to detect arrhythmias. The elaboration of the network was developed step by step and it is explained how to identify overfitting and how to correct it. The final accuracy of the algorithm was 81%.

The second manual stitches together a series of data previously recorded by Dr. McKiernan's students. In these data, there are recordings during short pulses of force and recordings during prolonged activations, all for both the right hand and the left hand. Filtered envelopes were first obtained for the EMG recordings. For pulse measurements, comparisons of EMG force vs. amplitude, main frequency vs. amplitude, and left vs. right-hand comparisons were made.

The third manual consists of a spirometry analysis in which all directly calculable respiratory volumes and capacities are obtained and amplitudes are compared with the envelope EMG signal.

Finally, the fourth manual consists of EEG analysis in pediatric patients with epilepsy. The data is freely accessible and can be downloaded from the site from the following link: https://openneuro.org/datasets/ds003555/versions/1.0.1/download. The data counts with 3 hours of measurement of 30 pediatric patients during sleep. All measurements are marked with the corresponding sleep stages. For the analysis, several sets of parameters were extracted and the efficiency of each was tested to identify the stage of sleep. Finally, an attempt was made to use seizure marking to train a program that could identify an epileptic seizure; however, the markings did not agree with electrophysiological expectations. Su uses cluster analysis to divide measurements into sleep phases and to estimate which segments contain an attack.

Thank you for visiting this repository. It was done with a lot of work and to serve those with an interest in exploring electrophysiological signals. I hope you find it useful.

# Prácticas computacionales y manuales experimentales para la enseñanza de Electrofisiología

Durante los últimos 6 meses estuve trabajando con la Dra. Erin McKiernan en la elaboración de manuales de código en Python con el objetivo de que sirvan para la enseñanza del análisis de señales electrofisiológicas. Se hicieron 4 conjuntos de manuales:

• Manual de análisis de electrocardiograma(ECG) con datos de pacientes con arritmia.

• Manual de análisis de electromiograma(EMG) con datos de activación en pulsos y de fatiga en ambas manos.

• Manual de análisis de espirometría con EMG de abdomen durante un protocolo de respiración con inspiración, inspiración forzada, expiración y expiración forzada.

• Manual de análisis de electroencefalograma(EEG) de pacientes pediátricos con epilepsia.

Todos los manuales se pueden encontrar en un repositorio de Github público (https://github.com/Javi-ciencias/Servicio_social).

Para el primer manual se importaron datos de libre acceso desde una base de datos en physionet(https://physionet.org/content/mitdb/1.0.0/). Primero se desarrolló un “notebook” que detectaba las ondas P, Q,R, S y T usando transformadas de Fourier y algoritmos de evaluación de puntos críticos. A partir de estos marcadores, calculaba parámetros importantes como la longitud del complejo QRS, ritmo cardíaco y la longitud de las ondas P y T. Los datos fueron alimentados a una red neuronal convolucional que se entrenó para detectar arritmias. Se desarrolló paso a paso la elaboración de la red y se explica cómo identificar un sobreajuste y cómo corregirlo. La precisión final del algoritmo fue del 81%.

El segundo manual cosiste en una serie de datos previamente grabados por los alumnos de la Dra. McKiernan. En estos datos se tienen grabaciones durante pulsos cortos de fuerza y grabaciones durante activaciones prolongadas, todo tanto para mano derecha, como mano izquierda. Primero se obtuvieron envolventes filtradas para las grabaciones de EMG. Para las mediciones de pulsos se hicieron comparaciones de fuerza contra amplitud de EMG, frecuencia principal contra amplitud y comparaciones entre mano izquierda y derecha.

El tercer manual consiste en un análisis de espirometría en el que se obtienen todos los volúmenes y capacidades respiratorias directamente calculables y se comparan amplitudes con la señal envolvente de EMG.

Finalmente, el cuarto manual consiste en análisis de EEG en pacientes pediátricos de con epilepsia. Los datos son de libre acceso y se pueden descargar en el sitio desde la siguiente liga: https://openneuro.org/datasets/ds003555/versions/1.0.1/download. Los datos cuentas con 3 horas de medición de 30 pacientes pediátricos durante el sueño. Todas las mediciones están marcadas con las etapas de sueño correspondientes. Para el análisis se extrajeron varios conjuntos de parámetros y se probó la eficiencia de cada uno para identificar la etapa de sueño. Finalmente, se intentó usar el marcaje de ataques para entrenar un programa que pudiera identificar un ataque epiléptico; sin embargo, los marcajes no concordaban con las expectativas electrofisiológicas. Su utiliza análisis de clústeres para dividir las mediciones en fases de sueño y para hacer una estimación de cuáles segmentos contienen un ataque.

Gracias por visitar este repositorio. Se realizó con mucho trabajo y con la intención de que le sirva a aquellos con el inetrés de explorar señales electrofisiológicas. Espero que te sea útil. 



