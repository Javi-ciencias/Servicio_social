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

Gracias por visitar este repositorio. Se realizó con mucho trabajo y con la intención de que le sirva a aquellos que les llame la atención el análisis de señales electrofisiológicas. Espero que te sea útil. 
:)
