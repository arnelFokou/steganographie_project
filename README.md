Documentation du projet : Stéganographie sur images en Python
Description du projet

Ce projet consiste en l’implémentation d’une stéganographie dans des images en utilisant la méthode des bits de poids faible (LSB). L’objectif principal était de créer un outil capable de cacher un message texte à l’intérieur d’une image et de pouvoir le récupérer ensuite sans altérer visiblement l’image.

Le projet est entièrement écrit en Python et fonctionne sur des images PNG au format standard (RGB). Il a été conçu pour être simple, clair et pédagogique.

Fonctionnalités implémentées

Insertion d’un message dans une image

Chaque pixel de l’image est composé de trois canaux (R, G, B).

Les bits de poids faible de chaque canal sont modifiés pour contenir les bits du message à cacher.

Avant insertion, les bits de poids faible sont mis à zéro pour garantir que le message peut être inséré correctement.

Extraction d’un message depuis une image

Lecture des bits de poids faible des pixels dans le même ordre que pour l’insertion.

Reconstruction du message original à partir des bits récupérés.

Gestion complète des caractères imprimables

Tous les caractères du message restent visibles après extraction.

La méthode évite les problèmes liés aux caractères non imprimables car tous les caracteres sont codes sur 21 bits reprsentant la longueur du plus grand caractere dans unicode.

Préparation des pixels pour le message

Les valeurs de tous les canaux sont rendues paires avant l’insertion.

Cela garantit que chaque bit du message peut remplacer le bit de poids faible sans erreur.

Fonctionnement général

Encodage du message

Le message texte est converti en suite binaire.

Chaque bit du message est inséré dans le bit de poids faible d’un canal de pixel de l’image.

Décodage du message

Les bits de poids faible des pixels sont extraits.

Ces bits sont recombinés pour reconstruire le message texte original.

Points forts du projet

Manipulation des images en Python sans dépendances externes complexes.

Maintien de l’apparence visuelle de l’image : les modifications sont invisibles à l’œil nu.

Fonctionne pour tout texte composé de caractères imprimables.

Code modulable et prêt à être utilisé pour d’autres projets de stéganographie ou d’enseignement.

Conclusion

Ce projet fournit une implémentation complète de la stéganographie dans les images :

Il permet de cacher et récupérer un message texte dans une image.

Il prépare les pixels pour une insertion sûre des bits du message.

Il gère correctement tous les caractères imprimables et préserve l’apparence de l’image.
