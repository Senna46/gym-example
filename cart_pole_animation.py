import gym
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#CarPoleの読み取りセット
env = gym.make("CartPole-v1", render_mode="rgb_array")
observation = env.reset()

fig = plt.figure()  # Figureオブジェクトを作成
ims = []            # 描画結果のフレームを格納するリスト（初期化）

#実行
for i in range(1000):
    #右に押す
    action = env.action_space.sample()

    #情報を取得
    observation, reward, terminated, truncated, info = env.step(action) 
    print("observation = " + str(observation))
    print("reward = " + str(reward))
    if terminated or truncated:
        if terminated:
            print("========terminated========")
            im=plt.text(0, 0, "1. terminated", fontsize=20)
            ims.append([im])
        if truncated:
            print("~~~~~~~~~truncated~~~~~~~~~")
            im=plt.text(0, 0, "2. truncated", fontsize=20)
            ims.append([im])
        
        observation, info = env.reset()

    #グラフ表示
    im=plt.imshow(env.render())
    #グラフを配列 ims に追加
    ims.append([im]) 

ani = animation.ArtistAnimation(fig, ims, interval=500)
plt.axis('off')
plt.show()

env.close()
