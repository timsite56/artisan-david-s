# -*- coding: utf-8 -*-
"""Contenu local des pages service × ville — Artisan David S.
Chaque couple (service, ville) a un texte d'introduction et une question
de FAQ qui lui sont propres : c'est ce qui évite le contenu dupliqué."""

VILLES = {
 "lorient": dict(
  nom="Lorient", cp="56100", dans="à Lorient", de="de Lorient",
  acces="20 min depuis Plouhinec, par la RN165",
  jardins="Parcelles de ville compactes, haies persistantes",
  attention="Accès étroits : matériel compact, évacuation incluse",
  hub_intro=[
   "Lorient a été presque entièrement reconstruite après 1945 : ses quartiers de pavillons — Keryado, Merville, Kerentrech, Carnel ou Lanveur — alternent petites parcelles, jardins de ville et haies persistantes plantées pour se protéger du vent d'ouest qui remonte la rade.",
   "<strong>Artisan David S</strong> intervient à Lorient pour l'élagage, la taille de haies, l'entretien de jardin, le débroussaillage et l'aménagement paysager. Installés à Plouhinec, nous sommes à une vingtaine de minutes de la ville : devis sur place gratuit et réponse rapide.",
  ],
  contexte="À Lorient, les jardins sont souvent enclavés entre deux maisons, avec un accès par un portillon ou un garage. Nous venons avec du matériel compact, nous broyons sur place quand c'est possible et nous évacuons tout : vous n'avez rien à porter en déchetterie.",
  faq=[
   ("Vous déplacez-vous dans tous les quartiers de Lorient ?", "Oui : centre-ville, Keryado, Merville, Kerentrech, Carnel, Lanveur, Bois-du-Château… et dans les communes voisines comme Lanester, Plœmeur, Larmor-Plage ou Quéven. Le déplacement pour le devis est gratuit."),
   ("Mon jardin n'a pas d'accès pour un véhicule, est-ce un problème ?", "Non. C'est fréquent à Lorient. Nous travaillons avec du matériel portatif, nous sortons les déchets en sacs ou en big-bags, et nous broyons sur place quand la place le permet."),
  ]),
 "vannes": dict(
  nom="Vannes", cp="56000", dans="à Vannes", de="de Vannes",
  acces="35 min depuis Plouhinec, par la RN165",
  jardins="Grands jardins, chênes, pins et cèdres",
  attention="Arbres protégés au PLU : vérification avant abattage",
  hub_intro=[
   "Préfecture du Morbihan et porte du golfe, Vannes compte de nombreux grands jardins : propriétés de Conleau et d'Arcal, maisons de Saint-Guen ou de Kercado, où poussent chênes, pins maritimes et cèdres plantés il y a plusieurs décennies.",
   "<strong>Artisan David S</strong> se déplace à Vannes et dans les communes du golfe — Séné, Arradon, Saint-Avé, Ploeren — pour l'élagage et l'abattage des grands arbres, la taille des haies, l'entretien régulier des jardins, le débroussaillage et l'aménagement paysager.",
  ],
  contexte="À Vannes, beaucoup de grands arbres sont repérés au plan local d'urbanisme, et le centre historique relève d'un secteur protégé. Avant tout abattage ou élagage important, nous vérifions avec vous ce qui est autorisé et, si besoin, la démarche à faire en mairie.",
  faq=[
   ("Intervenez-vous autour du golfe, pas seulement à Vannes ?", "Oui : Séné, Arradon, Saint-Avé, Ploeren, Theix-Noyalo, Baden… Nous regroupons les interventions du secteur pour garder des délais courts."),
   ("Mon arbre est-il protégé ?", "C'est possible : le PLU de Vannes protège certains arbres et boisements, et le centre ancien est en secteur patrimonial. Nous faisons le point avec vous avant d'intervenir et vous indiquons la démarche en mairie si elle est nécessaire."),
  ]),
 "auray": dict(
  nom="Auray", cp="56400", dans="à Auray", de="d'Auray",
  acces="20 min depuis Plouhinec",
  jardins="Terrains en pente, murets de pierre, vieux arbres",
  attention="Pentes vers la rivière : taille et évacuation adaptées",
  hub_intro=[
   "Entre le port de Saint-Goustan et les coteaux de la rivière d'Auray, les jardins alréens sont souvent en pente, bordés de murets de pierre, avec de vieux chênes et châtaigniers qui dominent les maisons anciennes.",
   "<strong>Artisan David S</strong> intervient à Auray et alentour — Brech, Pluneret, Crach, Pluvigner — à une vingtaine de minutes de notre base de Plouhinec : élagage, taille de haies, entretien, débroussaillage et aménagement de jardin.",
  ],
  contexte="À Auray, beaucoup de terrains descendent vers la rivière ou sont tenus par des murets anciens. Nous adaptons la méthode : travail encordé si nécessaire, protection des murets, évacuation des déchets sans abîmer les pelouses en pente.",
  faq=[
   ("Travaillez-vous sur des terrains très pentus ?", "Oui. C'est courant sur les coteaux d'Auray. Nous choisissons le matériel en conséquence et nous évacuons les déchets à la main ou au treuil si un engin ne peut pas descendre."),
   ("Intervenez-vous à Brech, Pluneret ou Crach ?", "Oui, ainsi qu'à Pluvigner, Locmariaquer et Belz. Ce sont des communes proches de notre base de Plouhinec."),
  ]),
 "hennebont": dict(
  nom="Hennebont", cp="56700", dans="à Hennebont", de="d'Hennebont",
  acces="15 min depuis Plouhinec",
  jardins="Coteaux boisés du Blavet, grands terrains",
  attention="Bords du Blavet : sols détrempés en hiver",
  hub_intro=[
   "Ville close au bord du Blavet, Hennebont mêle maisons anciennes, pavillons et grands terrains sur les coteaux boisés qui dominent la vallée. Les arbres y sont nombreux, les haies aussi, et la végétation pousse vite dans ce fond de vallée humide.",
   "<strong>Artisan David S</strong> est à un quart d'heure d'Hennebont : nous y réalisons l'élagage et l'abattage, la taille de haies, l'entretien de jardin, le débroussaillage de terrains et l'aménagement paysager, avec un devis gratuit sur place.",
  ],
  contexte="Sur les coteaux et en bordure du Blavet, les sols restent gorgés d'eau une partie de l'hiver. Nous planifions les gros travaux — abattage, débroussaillage, terrassement — hors des périodes les plus humides pour ne pas défoncer le terrain.",
  faq=[
   ("Êtes-vous vraiment à côté d'Hennebont ?", "Oui, à environ un quart d'heure. C'est l'un de nos secteurs les plus proches : nous pouvons souvent passer rapidement pour établir le devis."),
   ("Intervenez-vous aussi à Inzinzac-Lochrist, Languidic ou Kervignac ?", "Oui, toute la vallée du Blavet et les communes autour d'Hennebont font partie de notre zone d'intervention habituelle."),
  ]),
 "lanester": dict(
  nom="Lanester", cp="56600", dans="à Lanester", de="de Lanester",
  acces="20 min depuis Plouhinec",
  jardins="Lotissements, haies mitoyennes",
  attention="Haies en limite : règle des 2 m du code civil",
  hub_intro=[
   "Entre le Scorff et le Blavet, Lanester est une ville de lotissements : pavillons avec jardin, haies de clôture mitoyennes en laurier-palme, thuya ou cyprès de Leyland, qui prennent vite de la hauteur et de l'épaisseur.",
   "<strong>Artisan David S</strong> intervient à Lanester, à une vingtaine de minutes de Plouhinec, pour la taille et la réduction de haies, l'élagage, l'entretien régulier des jardins, le débroussaillage et l'aménagement paysager.",
  ],
  contexte="À Lanester, la plupart des haies sont plantées en limite de propriété. Le code civil fixe la règle : une plantation de plus de 2 mètres de haut doit être à au moins 2 mètres de la limite, sinon elle doit être maintenue sous 2 mètres. Nous taillons en conséquence pour éviter les litiges de voisinage.",
  faq=[
   ("Ma haie dépasse chez le voisin, que faire ?", "Les branches qui avancent chez le voisin doivent être coupées par le propriétaire de la haie. Nous taillons les deux faces si le voisin donne son accord, ou uniquement votre côté et le dessus sinon."),
   ("Intervenez-vous dans tous les quartiers de Lanester ?", "Oui, ainsi qu'à Caudan, Quéven et Lorient, juste à côté."),
  ]),
 "carnac": dict(
  nom="Carnac", cp="56340", dans="à Carnac", de="de Carnac",
  acces="20 min depuis Plouhinec",
  jardins="Résidences secondaires, pins maritimes, sol sableux",
  attention="Propriétaires absents : passages programmés, photos",
  hub_intro=[
   "Entre les alignements de menhirs et Carnac-Plage, une grande partie des maisons sont des résidences secondaires. Les jardins, plantés de pins maritimes et de haies qui supportent les embruns, poussent sans attendre le retour de leurs propriétaires.",
   "<strong>Artisan David S</strong> intervient à Carnac et sur la côte — La Trinité-sur-Mer, Plouharnel, Erdeven, Quiberon — pour l'entretien des jardins de résidences secondaires, l'élagage des pins, la taille des haies, le débroussaillage et l'aménagement paysager.",
  ],
  contexte="À Carnac, beaucoup de propriétaires ne sont là que quelques semaines par an. Nous programmons les passages à l'avance — avant l'arrivée des vacanciers, après la saison — et nous envoyons des photos après chaque intervention : vous savez où en est votre jardin sans vous déplacer.",
  faq=[
   ("Je n'habite pas à Carnac à l'année, comment ça se passe ?", "Nous convenons ensemble d'un calendrier de passages, vous nous laissez l'accès au jardin, et nous vous envoyons des photos après chaque intervention. Vous êtes prévenu par message avant et après."),
   ("Intervenez-vous aussi à La Trinité-sur-Mer et Quiberon ?", "Oui, ainsi qu'à Plouharnel, Erdeven, Locmariaquer et Saint-Philibert : toute la côte entre la ria d'Étel et la presqu'île de Quiberon."),
  ]),
}

ORDRE_VILLES = ["lorient", "vannes", "auray", "hennebont", "lanester", "carnac"]

SERVICES = {
 "elagage": dict(nom="Élagage et abattage", court="Élagage & abattage", page="elagage-abattage.html",
   img="images/service4.webp", titre="Élagage à {v} ({cp}) — élagueur, abattage d'arbres",
   h1="Élagage et abattage d'arbres {dans}", accroche="Élagueur {dans} : élagage d'entretien, taille de sécurité, abattage par démontage et dessouchage, avec évacuation complète des bois.",
   desc="Élagueur {dans} ({cp}) : élagage, abattage par démontage, dessouchage et évacuation. Devis gratuit, Noé 06 04 41 73 82 ou David 07 86 82 12 93."),
 "taille-de-haies": dict(nom="Taille de haies", court="Taille de haies", page="taille-de-haies.html",
   img="images/service5.webp", titre="Taille de haies à {v} ({cp}) — réduction, ramassage",
   h1="Taille de haies {dans}", accroche="Taille d'entretien, réduction de hauteur et d'épaisseur, haies mitoyennes : un travail net, déchets ramassés et évacués.",
   desc="Taille de haies {dans} ({cp}) : taille d'entretien, réduction de hauteur, haies mitoyennes, évacuation des déchets. Devis gratuit au 06 04 41 73 82."),
 "entretien-jardin": dict(nom="Entretien de jardin", court="Entretien de jardin", page="entretien-espaces-verts.html",
   img="images/service3.webp", titre="Entretien de jardin à {v} ({cp}) — jardinier paysagiste",
   h1="Entretien de jardin {dans}", accroche="Tonte, taille, désherbage, ramassage des feuilles : un entretien ponctuel ou à l'année, pour un jardin propre sans y passer vos week-ends.",
   desc="Entretien de jardin {dans} ({cp}) : tonte, taille, désherbage, ramassage des feuilles, contrat à l'année ou passage ponctuel. Devis gratuit au 06 04 41 73 82."),
 "debroussaillage": dict(nom="Débroussaillage et remise en état", court="Débroussaillage", page="debroussaillage-terrain.html",
   img="images/gallery4.webp", titre="Débroussaillage à {v} ({cp}) — terrain, évacuation",
   h1="Débroussaillage et remise en état de terrain {dans}", accroche="Terrain envahi de ronces, jardin laissé à l'abandon, maison à vendre ou succession : nous débroussaillons, dessouchons et évacuons tout.",
   desc="Débroussaillage {dans} ({cp}) : terrain en friche, ronces, jardin abandonné, maison à vendre. Remise en état et évacuation des déchets verts. Devis au 06 04 41 73 82."),
 "amenagement-paysager": dict(nom="Aménagement paysager", court="Aménagement paysager", page="amenagement-paysager.html",
   img="images/service2.webp", titre="Aménagement paysager à {v} ({cp}) — jardin, terrasse, clôture",
   h1="Aménagement paysager {dans}", accroche="Plantations, engazonnement, allées, clôtures et massifs : un jardin pensé pour votre terrain et le climat breton.",
   desc="Aménagement paysager {dans} ({cp}) : création de jardin, plantations, engazonnement, allées et clôtures. Devis gratuit, Noé 06 04 41 73 82 ou David 07 86 82 12 93."),
}

ORDRE_SERVICES = ["elagage", "taille-de-haies", "entretien-jardin", "debroussaillage", "amenagement-paysager"]

# (service, ville) -> (introduction propre, (question, réponse) propre)
COMBOS = {
 ("elagage", "lorient"): (
  "À Lorient, les arbres de jardin poussent souvent à quelques mètres des façades : un chêne ou un pin planté dans les années 1960 surplombe aujourd'hui la toiture du voisin. Face au vent d'ouest qui s'engouffre dans la rade, une branche morte ou un houppier trop chargé devient vite un risque. Nous réduisons, allégeons ou démontons par pièces, avec rétention au-dessus des toits et des clôtures.",
  ("Que faire d'un arbre qui menace ma maison après un coup de vent ?", "Appelez-nous : nous sécurisons d'abord les branches cassées ou pendantes, puis nous planifions l'élagage ou l'abattage. À Lorient, le démontage par pièces avec cordes est souvent la seule méthode possible entre deux maisons.")),
 ("elagage", "vannes"): (
  "Les grands jardins de Vannes — Conleau, Arcal, Saint-Guen — abritent des chênes, des pins maritimes et des cèdres de plusieurs dizaines de mètres. Ces sujets demandent un élagueur équipé pour la grimpe et le démontage, et une attention particulière aux règles locales : certains arbres sont repérés au PLU. Nous faisons le point avant d'intervenir, puis nous élaguons proprement, sans étêter.",
  ("Faut-il une autorisation pour abattre un arbre à Vannes ?", "Pas toujours, mais c'est à vérifier : le PLU de Vannes protège certains arbres et espaces boisés, et le centre historique est en secteur patrimonial. Nous regardons votre situation avant tout devis d'abattage.")),
 ("elagage", "auray"): (
  "À Auray, les vieux chênes et châtaigniers des coteaux de la rivière ont souvent été plantés bien avant les maisons qui les entourent. Sur ces terrains en pente, l'élagage se fait en grimpe encordée, et la descente des branches doit être maîtrisée pour épargner les murets de pierre et les toitures en contrebas.",
  ("Pouvez-vous élaguer un arbre au bord d'un muret en pierre ?", "Oui. Nous descendons les branches avec des cordes plutôt que de les laisser tomber, et nous protégeons le muret. C'est une configuration fréquente à Auray et à Saint-Goustan.")),
 ("elagage", "hennebont"): (
  "Sur les coteaux boisés qui dominent le Blavet, les arbres d'Hennebont grandissent vite et finissent par faire de l'ombre à tout le jardin. Nous éclaircissons les houppiers pour faire revenir la lumière, retirons le bois mort et abattons par démontage les sujets devenus dangereux, à un quart d'heure de notre base.",
  ("Mon terrain est très humide en hiver, pouvez-vous quand même intervenir ?", "Oui, mais nous choisissons le moment : en bord de Blavet, nous évitons les semaines les plus détrempées pour ne pas marquer le terrain avec le matériel. L'élagage en grimpe, lui, se fait sans problème.")),
 ("elagage", "lanester"): (
  "Dans les lotissements de Lanester, un arbre planté petit dans les années 1980 dépasse aujourd'hui le toit et avance chez les voisins. L'élagage de réduction permet de le garder en le ramenant à une taille raisonnable ; quand il est trop près de la maison ou des réseaux, nous l'abattons par démontage et dessouchons pour libérer la place.",
  ("Mon voisin se plaint de mon arbre, que dit la loi ?", "Les branches qui dépassent chez le voisin doivent être coupées par le propriétaire de l'arbre, et une plantation de plus de 2 mètres doit être à au moins 2 mètres de la limite. Nous réduisons l'arbre pour vous mettre en règle.")),
 ("elagage", "carnac"): (
  "À Carnac, les pins maritimes font partie du paysage, mais ils supportent mal le manque d'entretien : branches mortes, sujets penchés par le vent, aiguilles qui bouchent les gouttières. Nous élaguons et sécurisons les pins de votre résidence, même en votre absence, et nous vous envoyons des photos avant et après.",
  ("Pouvez-vous élaguer mes pins pendant que je ne suis pas là ?", "Oui. C'est même le cas le plus courant à Carnac : nous convenons de la date, vous nous laissez l'accès, et vous recevez les photos de l'intervention.")),

 ("taille-de-haies", "lorient"): (
  "À Lorient, les haies de laurier-palme, de photinia ou de thuya servent de coupe-vent et de brise-vue sur des parcelles souvent petites. Elles poussent vite dans le climat doux de la rade et mangent le jardin si on les laisse faire. Nous les taillons droites et nettes, deux fois par an si nécessaire, et nous repartons avec les déchets.",
  ("Combien de fois par an tailler une haie de laurier à Lorient ?", "Deux tailles par an sont l'idéal : une au printemps et une à la fin de l'été ou en automne. Le climat doux de Lorient fait pousser le laurier-palme très vite.")),
 ("taille-de-haies", "vannes"): (
  "Autour de Vannes, les haies marquent les limites de grands terrains : parfois plusieurs dizaines de mètres de linéaire, en charmille, en laurier ou en essences variées. Nous intervenons avec du matériel adapté aux grandes longueurs et à la hauteur, pour une taille régulière sur toute la haie, et nous évacuons l'ensemble des déchets.",
  ("Pouvez-vous tailler une très grande haie en une seule fois ?", "Oui. Pour les grands linéaires que l'on trouve à Vannes et dans le golfe, nous venons à plusieurs avec du matériel en hauteur, et le chantier est terminé dans la journée dans la plupart des cas.")),
 ("taille-de-haies", "auray"): (
  "À Auray, beaucoup de haies sont plantées au sommet d'un talus ou en haut d'un muret, ce qui complique l'accès pour les tailler. Nous travaillons avec des échafaudages légers ou des perches selon la configuration, pour obtenir une taille propre sans abîmer le muret ni la pelouse en pente.",
  ("Ma haie est sur un talus, pouvez-vous la tailler ?", "Oui. C'est très fréquent à Auray. Nous adaptons le matériel (perches, plateformes) pour atteindre le haut et la face côté route en toute sécurité.")),
 ("taille-de-haies", "hennebont"): (
  "À Hennebont, les haies bocagères et les haies de pavillon profitent de l'humidité de la vallée du Blavet : elles s'épaississent vite et empiètent sur les allées et les trottoirs. Nous réduisons l'épaisseur, reprenons la hauteur et redonnons une forme régulière, à un quart d'heure de chez nous.",
  ("Ma haie déborde sur le trottoir, suis-je obligé de la tailler ?", "Oui : la haie ne doit pas empiéter sur la voie publique. Nous la ramenons à l'aplomb de votre limite et évacuons tous les déchets.")),
 ("taille-de-haies", "lanester"): (
  "À Lanester, la haie est souvent mitoyenne et fait l'objet de discussions entre voisins. Le code civil impose qu'une haie plantée à moins de 2 mètres de la limite soit maintenue sous 2 mètres de haut. Nous taillons à la bonne hauteur et, avec l'accord du voisin, des deux côtés.",
  ("Quelle hauteur pour une haie en limite de propriété ?", "Si la haie est plantée à moins de 2 mètres de la limite, elle doit rester sous 2 mètres de haut (article 671 du code civil). Au-delà de 2 mètres de la limite, elle peut être plus haute.")),
 ("taille-de-haies", "carnac"): (
  "À Carnac, les haies de tamaris, d'escallonia ou de pittosporum protègent les jardins des embruns. Dans une résidence secondaire, elles poussent tout l'hiver sans que personne ne les voie. Nous passons avant la saison pour que tout soit net à votre arrivée, et vous recevez une photo du résultat.",
  ("Quand tailler la haie de ma maison de vacances à Carnac ?", "Idéalement en fin d'hiver ou au début du printemps, avant l'arrivée des vacanciers, puis une seconde fois en fin d'été. Nous calons les dates avec vous.")),

 ("entretien-jardin", "lorient"): (
  "À Lorient, un jardin de ville se transforme vite en jungle entre avril et octobre. Nous proposons des passages réguliers — tonte, taille des arbustes, désherbage manuel, nettoyage des massifs — ou une remise au propre ponctuelle, pour un jardin toujours présentable sans y consacrer vos week-ends.",
  ("Proposez-vous un entretien régulier à Lorient ?", "Oui : un passage toutes les deux ou trois semaines en saison, plus espacé en hiver. Le prix est fixé à l'avance selon la surface et les travaux inclus.")),
 ("entretien-jardin", "vannes"): (
  "Les grands jardins de Vannes demandent du temps : pelouses étendues, massifs, feuilles des grands arbres à ramasser chaque automne. Nous prenons en charge l'entretien complet, à l'année ou à la saison, avec un calendrier fixé ensemble et une équipe qui connaît votre jardin.",
  ("Ramassez-vous les feuilles des grands arbres ?", "Oui. À Vannes, le ramassage des feuilles de chênes et de platanes est un gros poste à l'automne : nous le faisons en un ou deux passages et évacuons tout.")),
 ("entretien-jardin", "auray"): (
  "À Auray, les jardins en pente et les vieux murets demandent un entretien soigneux : tonte sur terrain incliné, désherbage des pieds de murs, taille des arbustes qui envahissent les escaliers. Nous intervenons régulièrement ou ponctuellement, avec le matériel adapté aux pentes.",
  ("Pouvez-vous tondre un terrain en forte pente ?", "Oui, avec des tondeuses et débroussailleuses adaptées. Sur les pentes les plus fortes d'Auray, nous passons à la débroussailleuse pour un résultat propre et sans risque.")),
 ("entretien-jardin", "hennebont"): (
  "À Hennebont, l'humidité de la vallée du Blavet fait pousser l'herbe et les haies à grande vitesse. Un entretien régulier évite de se laisser déborder : tonte, taille, désherbage manuel des allées et ramassage des feuilles, par une équipe basée à un quart d'heure.",
  ("Désherbez-vous sans produits chimiques ?", "Oui. Depuis 2019, les particuliers ne peuvent plus utiliser de pesticides de synthèse dans leur jardin : nous désherbons manuellement ou mécaniquement.")),
 ("entretien-jardin", "lanester"): (
  "Dans les pavillons de Lanester, le jardin est souvent de taille moyenne mais demande un passage régulier : tonte, taille de la haie, nettoyage des massifs. Nous proposons des formules simples, avec un prix connu d'avance, pour ne plus avoir à s'en occuper.",
  ("Combien coûte l'entretien d'un jardin de pavillon ?", "Cela dépend de la surface et de ce qui est inclus (tonte seule, ou tonte et taille). Nous passons voir votre jardin à Lanester et vous remettons un devis gratuit et précis.")),
 ("entretien-jardin", "carnac"): (
  "À Carnac, l'entretien d'une résidence secondaire se fait sans le propriétaire : nous passons selon un calendrier défini ensemble, tondons, taillons, nettoyons les allées et ramassons les aiguilles de pin, puis nous vous envoyons des photos. Votre jardin est prêt à chaque séjour.",
  ("Pouvez-vous entretenir mon jardin toute l'année en mon absence ?", "Oui. C'est notre formule la plus demandée à Carnac : passages programmés, photos après chaque intervention, et un contact direct avec Noé ou David.")),

 ("debroussaillage", "lorient"): (
  "À Lorient, une parcelle laissée à l'abandon quelques années se couvre de ronces, de lierre et de jeunes arbres. Avant une vente, une location ou des travaux, nous débroussaillons, arrachons les souches et évacuons tous les déchets : le terrain retrouve sa surface utile et sa valeur.",
  ("Pouvez-vous remettre en état un jardin avant une vente à Lorient ?", "Oui. Nous débroussaillons, taillons, évacuons les déchets verts et rendons le terrain présentable pour les visites. Un jardin propre aide à vendre plus vite.")),
 ("debroussaillage", "vannes"): (
  "Autour de Vannes, de nombreux terrains en périphérie — Saint-Avé, Séné, Ploeren — restent en friche entre deux projets : ronces, ajoncs, fougères et jeunes arbres. Nous les débroussaillons à la débroussailleuse et au broyeur, dessouchons si nécessaire et laissons un terrain prêt à construire ou à aménager.",
  ("Faut-il débroussailler un terrain avant de construire ?", "Oui, le terrain doit être dégagé avant l'implantation. Nous débroussaillons, dessouchons et évacuons les déchets pour que le terrassement puisse commencer.")),
 ("debroussaillage", "auray"): (
  "À Auray, les terrains en pente vers la rivière sont vite envahis par les ronces et les ajoncs, difficiles d'accès pour un engin. Nous débroussaillons au matériel portatif, dégageons les murets et escaliers enfouis sous la végétation et évacuons les déchets même quand aucun véhicule ne peut descendre.",
  ("Mon terrain est inaccessible aux engins, pouvez-vous le débroussailler ?", "Oui. Nous travaillons à la débroussailleuse et à la tronçonneuse, et nous remontons les déchets à la main. C'est plus long, mais aucun terrain n'est impossible.")),
 ("debroussaillage", "hennebont"): (
  "Autour d'Hennebont, les grands terrains sur les coteaux du Blavet et les fonds de parcelles boisés reprennent vite leur état sauvage. Nous remettons en état : débroussaillage, abattage des petits arbres, dessouchage et évacuation, pour retrouver un terrain utilisable.",
  ("Que faites-vous des déchets verts ?", "Nous les broyons sur place quand c'est possible, et nous évacuons le reste vers une filière de valorisation. Le brûlage des déchets verts est interdit aux particuliers.")),
 ("debroussaillage", "lanester"): (
  "À Lanester, le débroussaillage concerne souvent un fond de jardin oublié, un talus en limite ou une parcelle de succession. Nous nettoyons tout — ronces, lierre, bambous, souches — et vous rendons un terrain propre, déchets compris.",
  ("Pouvez-vous nettoyer le jardin d'une maison de succession ?", "Oui. Nous intervenons souvent pour des familles qui doivent vider et remettre en état une maison : débroussaillage, taille, évacuation des déchets verts, et nous pouvons aussi débarrasser les encombrants du jardin.")),
 ("debroussaillage", "carnac"): (
  "À Carnac, une résidence secondaire peu entretenue se couvre de ronces et d'herbes hautes dès la fin du printemps, ce qui augmente aussi le risque d'incendie l'été. Nous débroussaillons avant la saison, évacuons tout et pouvons ensuite assurer l'entretien régulier en votre absence.",
  ("Faut-il débroussailler avant l'été ?", "C'est fortement conseillé : les herbes sèches et les ronces sont un risque d'incendie en été sur la côte. Un débroussaillage au printemps garde le terrain sûr et présentable.")),

 ("amenagement-paysager", "lorient"): (
  "À Lorient, un petit jardin bien pensé vaut mieux qu'un grand jardin mal organisé. Nous aménageons les parcelles de ville : terrasse, massifs persistants résistants au vent, allée, brise-vue végétal, gazon. Chaque mètre carré est utilisé, avec des plantes adaptées à l'air salin de la rade.",
  ("Quelles plantes résistent au vent et au sel à Lorient ?", "Escallonia, pittosporum, griselinia, tamaris ou éléagnus supportent bien le vent et les embruns. Nous choisissons les végétaux en fonction de l'exposition exacte de votre jardin.")),
 ("amenagement-paysager", "vannes"): (
  "Autour de Vannes et du golfe, les projets d'aménagement portent souvent sur de grands terrains : création de massifs, plantation d'arbres, engazonnement, allées et clôtures. Nous concevons un plan adapté au terrain et au budget, puis nous réalisons les travaux par étapes si vous le souhaitez.",
  ("Pouvez-vous aménager le jardin d'une maison neuve ?", "Oui. Après la construction, nous nivelons, engazonnons, plantons les haies et arbres, créons les allées et posons les clôtures. Nous pouvons étaler le chantier sur plusieurs saisons.")),
 ("amenagement-paysager", "auray"): (
  "À Auray, un terrain en pente se transforme en atout : paliers, escaliers en pierre, massifs en restanque, plantations qui retiennent la terre. Nous aménageons les jardins des coteaux en respectant les murets existants et le caractère des maisons anciennes.",
  ("Comment aménager un jardin en pente ?", "En créant des paliers, en plantant des couvre-sols qui retiennent la terre et en aménageant des accès sûrs. Nous vous proposons un plan adapté à la pente de votre terrain à Auray.")),
 ("amenagement-paysager", "hennebont"): (
  "À Hennebont, les grands terrains des coteaux du Blavet offrent de la place pour un vrai projet : pelouse, verger, haies bocagères, massifs, allées. Nous aménageons en tenant compte de l'humidité des sols et de l'exposition, pour des plantations qui reprennent bien.",
  ("Quelle est la meilleure période pour planter ?", "L'automne, de fin octobre à décembre, est la meilleure saison pour planter arbres, arbustes et haies : les racines s'installent pendant l'hiver.")),
 ("amenagement-paysager", "lanester"): (
  "À Lanester, beaucoup de jardins de pavillon n'ont jamais été aménagés depuis la construction. Nous refaisons l'ensemble : remplacement d'une haie de thuyas vieillissante, nouvelle pelouse, massifs faciles d'entretien, clôture et portillon, pour un jardin agréable sans contraintes.",
  ("Pouvez-vous remplacer une vieille haie de thuyas ?", "Oui : nous arrachons la haie, dessouchons, préparons le sol et replantons une haie variée, plus résistante et plus facile à entretenir.")),
 ("amenagement-paysager", "carnac"): (
  "À Carnac, un jardin de résidence secondaire doit être beau et demander peu d'entretien. Nous aménageons avec des plantes adaptées au sol sableux et aux embruns, des paillages qui limitent l'arrosage et les mauvaises herbes, et des allées qui ne s'entretiennent presque pas.",
  ("Quel jardin pour une maison de vacances à Carnac ?", "Un jardin sobre : graminées, plantes de bord de mer, paillage minéral ou végétal, peu de gazon. Il reste beau toute l'année avec deux ou trois passages d'entretien.")),
}

# Nouvelle page service : débroussaillage (n'existait pas sur le site)
DEBROUSSAILLAGE = dict(
 checks=[
  ("Débroussaillage de terrain", "Ronces, ajoncs, fougères, herbes hautes : terrain dégagé à la débroussailleuse et au broyeur."),
  ("Jardin laissé à l'abandon", "Remise au propre complète d'un jardin non entretenu depuis des années."),
  ("Avant une vente ou une location", "Terrain rendu présentable pour les visites et l'état des lieux."),
  ("Maison de succession", "Remise en état du jardin, et débarras des encombrants extérieurs si besoin."),
  ("Abattage et dessouchage", "Petits arbres, bambous et souches retirés pour récupérer la surface."),
  ("Évacuation des déchets verts", "Broyage sur place ou évacuation en filière de valorisation, rien ne reste sur le terrain."),
 ],
 steps=[
  ("Visite du terrain", "Nous évaluons la surface, la végétation et l'accès pour les engins."),
  ("Devis clair", "Débroussaillage, dessouchage et évacuation chiffrés séparément."),
  ("Intervention", "Débroussailleuse, tronçonneuse et broyeur : le terrain est dégagé."),
  ("Terrain rendu propre", "Déchets évacués, souches traitées, surface prête à l'usage."),
 ],
 faq=[
  ("Le brûlage des déchets verts est-il autorisé ?", "Non : le brûlage des déchets verts est interdit aux particuliers. Nous broyons sur place ou évacuons vers une filière de valorisation."),
  ("Combien coûte le débroussaillage d'un terrain ?", "Le prix dépend de la surface, de la densité de la végétation et de l'accès. Nous passons voir le terrain et vous remettons un devis gratuit."),
  ("Pouvez-vous aussi débarrasser les encombrants du jardin ?", "Oui. Vieux mobilier de jardin, gravats légers, ferraille : nous pouvons les évacuer en même temps que les déchets verts."),
 ],
)
