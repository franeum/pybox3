Esame di Sistemi e linguaggi di programmazione per l'audio e le applicazioni musicali I
=======================================================================================

1. Le prove prevedono la stesura di script in python che saranno verificati su pybox. Per ogni esercizio si realizzi uno script dedicato, quindi lo studente consegnerà tanti script quanti sono gli esercizi da lui realizzati;
2. La documentazione del *package* **pybox** si trova a questo indirizzo: https://franeum.github.io/pybox3/modules.html;
3. Il termine ultimo per la presentazione degli script è il 14 Ottobre 2025 alle ore 23:59;
4. Gli script, raccolti in un unico file *zip*, devono essere spediti via e-mail all'indirizzo del docente;
5. L'esercizio 5 è facoltativo. Serve eventualmente per la lode, oppure come sostituto in caso di difficoltà su un altro esercizio;
6. La valutazione terrà conto, per ogni script, dei seguenti parametri:

+--------------------------------------+-------------------+
| parametro                            | massimo punteggio |
+======================================+===================+
| logica                               | 3                 |
+--------------------------------------+-------------------+
| commenti (efficacia ed espressività) | 2                 |
+--------------------------------------+-------------------+
| spaziatura e stile                   | 1                 |
+--------------------------------------+-------------------+
| espressività delle etichette         | 1.5               |
+--------------------------------------+-------------------+


====


001 - Diagonale
---------------

Realizzare il comportamento in figura, con le seguenti caratteristiche:

1. colore dei pixel: rosso
2. intervallo: 250 *millisecondi*

.. image:: _static/exam/001_diagonale.gif
  :class: bordered-img
  :align: center

====

002 - Push
----------

Realizzare un meccanismo che permetta di accendere il pixel con indice *12* finché il pulsante 1 sia premuto, altrimenti lo tenga spento. Vedi figura.

.. container:: image-row

  .. image:: _static/exam/002_push.gif
    :class: inline-img

  .. image:: _static/exam/002_push_pixel.gif
    :class: bordered-img inline-img

====

003 - Encoder
-------------

Realizzare il seguente comportamento: 

1. La rotazione di un encoder permette di muovere un pixel all'interno della matrice. 
2. La rotazione in senso orario sposta i pixel verso destra (cioè ogni *tick* dell'encoder aumenta di 1), mentre un *tick* in senso antiorario diminuisce il conteggio di 1.
3. Il pixel in movimento è verde

.. container:: image-row

  .. image:: _static/exam/003_encoder_drive.gif
    :class: inline-img

  .. image:: _static/exam/003_encoder.gif
    :class: bordered-img inline-img

====

004 - Toggle
------------

Realizzare il seguente comportamento: 

1. La pressione del pulsante alterna l'accensione e lo spegnimento di un led (oggetto della classe LED)
3. Il colore del led è blu.

.. container:: image-row

  .. image:: _static/exam/004_push_rele.gif
    :class: inline-img

  .. image:: _static/exam/004_push_rele_pixel.gif
    :class: bordered-img inline-img

====

005 - Bonux Track
-----------------

Traccia facoltativa: Realizzare il comportamento in figura. 

1. Il *cerchio* è gestito da un encoder.
2. Se ruotato in senso orario si completa, altrimenti scompare.
3. Il colore del cerchio è rosso.

.. container:: image-row

  .. image:: _static/exam/animazione.gif
    :class: inline-img

  .. image:: _static/exam/005_bonus.gif
    :class: bordered-img inline-img