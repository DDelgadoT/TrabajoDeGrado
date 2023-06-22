from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('distilbert-base-nli-mean-tokens')

sentencesQ1 = [
    'during the wintertime, outdoor enthusiasts can enjoy skiing or snowboarding down the steep slope of a mountain, breathing in the crisp cloudless air as they carve their way along the winding trail',
    'the location of the trail is cloudless and wintertime in outdoor',
    'the mountainside area is covered by a snowman called the mountainside',
    'the two types of coldness in winter are cold weather and snow',
    'there is a place to go with the family to eat at a temperature of minus 30 degrees called slope'
    ]
sentence_embeddings_q1 = model.encode(sentencesQ1)

print("Pregunta 1")
print(util.pytorch_cos_sim(sentence_embeddings_q1[0], sentence_embeddings_q1[1])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q1[0], sentence_embeddings_q1[2])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q1[0], sentence_embeddings_q1[3])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q1[0], sentence_embeddings_q1[4])[0][0])
print()

sentencesQ2 = [
    'the coral reef is a thriving ecosystem, teeming with life both in the clear waters above and in the earth beneath, while gaseous bubbles rise up from the well below, reminding us of the intricate connections that exist between the land, water, and atmosphere',
    'the innate coral reef fish is an innate part of water',
    'the pond is made from stony coral',
    'the rocker is amphibian and coral reef nature',
    'the well-known coral reef is located in the earth of the gaseous'
    ]
sentence_embeddings_q2 = model.encode(sentencesQ2)

print("Pregunta 2")
print(util.pytorch_cos_sim(sentence_embeddings_q2[0], sentence_embeddings_q2[1])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q2[0], sentence_embeddings_q2[2])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q2[0], sentence_embeddings_q2[3])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q2[0], sentence_embeddings_q2[4])[0][0])
print()

sentencesQ3 = [
    'on any common avenue or quiet street, one might catch a glimpse of a sleek car gliding beneath the starry night sky, a fleeting reminder of the endless possibilities that await beyond our everyday routine',
    'the street name of the street with the common name of "arth is "street"',
    'the location of the car with a ray of the sky is apartment',
    'the natural name of the building in the city of door is natural',
    'the wheel is a transport vehicle for the angel sky'
    ]
sentence_embeddings_q3 = model.encode(sentencesQ3)

print("Pregunta 3")
print(util.pytorch_cos_sim(sentence_embeddings_q3[0], sentence_embeddings_q3[1])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q3[0], sentence_embeddings_q3[2])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q3[0], sentence_embeddings_q3[3])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q3[0], sentence_embeddings_q3[4])[0][0])
print()

sentencesQ4 = [
    'standing in the middle of a big, lively crowd, it\'s easy to feel both small and alive at the same time, a single person fitting into a greater tapestry of humanity',
    'the musical genre of the musician who plays the violin is well established',
    'the crowd is suited for a place with the full name of "live"',
    'impersonate is an event for the whole family',
    'the crowd is popular with the popular musical genre of "move in concert"'
    ]
sentence_embeddings_q4 = model.encode(sentencesQ4)

print("Pregunta 4")
print(util.pytorch_cos_sim(sentence_embeddings_q4[0], sentence_embeddings_q4[1])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q4[0], sentence_embeddings_q4[2])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q4[0], sentence_embeddings_q4[3])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q4[0], sentence_embeddings_q4[4])[0][0])
print()

sentencesQ5 = [
    'the metro is a marvel of mechanical transport, whisking commuters from one crossing of the city to another with efficient and reliable transportage',
    'gunpowder was a builder of the railroad',
    'the railroad\'s hold the title of "trick" and "trail is hold by talent',
    'the train station has a rapid glow',
    'the metro has a mechanical gearbox and a transport system, which is a type of transport of transport'
    ]
sentence_embeddings_q5 = model.encode(sentencesQ5)

print("Pregunta 5")
print(util.pytorch_cos_sim(sentence_embeddings_q5[0], sentence_embeddings_q5[1])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q5[0], sentence_embeddings_q5[2])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q5[0], sentence_embeddings_q5[3])[0][0])
print(util.pytorch_cos_sim(sentence_embeddings_q5[0], sentence_embeddings_q5[4])[0][0])
print()