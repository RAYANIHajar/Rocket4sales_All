# Rocket4sales_All

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# Instruction 1 :
Comme le travail demandé est le redressement de la donnée sur l'onglet "Liste de comptes", donc j'ai opter pour deux méthode:

Méthode 1 :

L'utilisation du studio Talend qui supporte les projets ETL et ELT avec son interface graphique qui offre une représentation visuelle des flux de données de l'organisation. Pour notre cas, j'ai créé un nouveau job talend pour but de créer une table dans la base de données qui contiendera les élement LinkedUrl, CompanyID et les autres élements de la feuille qui correspondent à chanque E/se. tout en ajoutant un fichier 'erreur' qui contien les lignes qui n'ont pas une valeur (companyID ou LinkedUrl) correspondante.

Méthode 2 :

L'utilisation de Pandas qui est une bibliothèque open-source permettant la manipulation et l’analyse de données de manière simple et intuitive en Python. Donc après l'importation de notre fichier excel et la lecture de chacune de ses sheets, j'ai opter pour le cleaning de ma data en supprimant les doublons (colonne 'name') et en calculant le nbre de missing data, puis j'ai fait une jointure entre les deux sheets (df) ; Liste de comptes et company_Info pour récuperer les urls et les ID. Et pour les missing data que j'ai trouver j'ai opter par une solution pour les récupérer, qui est le webscraping using la bibliotheque beautifulSoup puisque j'ai parsé les données depuis google où le contenu html est prêt à être utilisé (server side rendering), et donc je peux trouver directement le lien linkedIn de E/se, et pour le 'companyID' se fera de la même manière mais cette fois-ci using selenium library.

Une dérniere méthode que j'ai utiliser est PowerBI Desktop dont j'ai opté pour PowerQuery en premier pour la suppression des doublons pour la colonne 'name' de la table company_Info eépour que je puisse faire une liaison one-to-many en utilisant powerpivot entre mes deux tables (company_Info et liste des comptes), et finalement j'ai créé une nouvelle colonne:
CompanyURLLOOKupvalue = LOOKUPVALUE(Company_Info[companyURL],Company_Info[name],'Liste de comptes'[Account Name]).

# Instruction 2 :
Cette instruction demande l'attrubution automatique des corrspondences pour les jobref en fonction des données contenues dans le sheet 'Linkedin job url', alors que la colonne (c) n'existe pas dans la feuille et si on suppose qu'on doit la créer à nouveau ça sera de la même manière que l'instruction 1 using Pandas, et donc par manque de temps j'ai opté pour une seule méthode qui est la jointure using talend, en créant une colonne 'JObTitle Correspendance' dans la feuile 'JobTitle Correspondance'. Mais il faut que vous sachiez que les mesures qui sont dans la colonne 'JObTitle Correspendance' => RECHERCHEV(C2;'JobTitle Correspondance'!A:B;3;) ont un empacement de valeur (3) et qui est normalement nul dans le sheet qu'on doit remplir, et si on le change par la colonne 2 qui est jobRef ça va retourner donc la même valeur que jobRef.

# Instruction 3 :
Cette fois-ci le travail demandé est la récupération des annonces faites sur le site 'welcom to the jugle', donc pour se faire j'ai opté pour le framework portable Selenium et cela parceque welcom to the jungle est ce qu'on application à page unique qui est une application qui interagit avec les utilisateurs en réécrivant les pages Web existantes avec de nouvelles données provenant du serveur Web, au lieu d’utiliser la technique par défaut du navigateur qui exécute une toute nouvelle page, c'est ce qu'on appel 'SINGLE PAGE APPLICATION', donc ici les données sont générées de manières asynchrone et du coup je dois attendre la création du Dom et des differents détails (liste des offres d'emploi et les liens pour acceder à la description...), donc cet outils va me permettre de simuler l'accès d'un human user. Donc comme debut j'ai commencé par scrapper la data existante dans la page contenant tout les offres. et puis je faisais une boucle pour acceder à chaque offre séparement de façon à ce que je peux scrapper les autres élements. Pour l'élement 'JobCorrespondance' je ne l'ai pas trouver sur la page et du coup je ne l'ai pas scrappé.

Après pour la partie stockage, j'ai stocké toutes les listes dans une dataFrame en ajoutant une liste remplie manuelle (juste pour raison de garder la même structure que le sheet pré-existant, et puis j'ai defini une fonction pour but de stocker la data dans le même sheet qui est 'wttj jobs offers'.
