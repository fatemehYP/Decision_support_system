import logging


def test():
    return int("foo")


try:
    test()
except:
    logging.exception("catch a error")



def init_page(root):
    frame_width = root.winfo_screenwidth()
    frame_height = root.winfo_screenheight()
    main_frame = tk.Frame(root, width=frame_width - 30, height=frame_height)
    # background_img = Image.open("images/background_image2.jpg")
    # resized_back_img = background_img.resize((frame_width, frame_height))
    # back_img = ImageTk.PhotoImage(resized_back_img)
    # img_1_lbl = tk.Label(main_frame, image=back_img)
    # img_1_lbl.grid(row=0, column=0, sticky="NESW")

    # img_1_lbl.place(relx=0.5, rely=0.5, sticky="center")
    # main_frame.grid_rowconfigure(0, weight=1)
    # main_frame.grid_rowconfigure(1, weight=1)
    # main_frame.grid_rowconfigure(2, weight=1)
    # main_frame.grid_columnconfigure(0, weight=1)
    # main_frame.grid_columnconfigure(1, weight=1)
    # main_frame.grid_columnconfigure(2, weight=1)
    print(main_frame.grid_size())
    main_frame.grid()
    # main_frame.place(relx=.5, rely=.5, anchor="center")

    pushing_frame = tk.Frame(main_frame, width=(frame_width - 100) / 3, height=400, bg="white")
    pushing_frame.config(borderwidth=6, relief="groove")
    # pushing_frame.place(relx=0.17, rely=0.5, anchor="center")

    pushing_frame.grid_rowconfigure(0, weight=1)
    pushing_frame.grid_rowconfigure(1, weight=1)
    pushing_frame.grid_rowconfigure(2, weight=1)
    pushing_frame.grid_columnconfigure(0, weight=1)
    pushing_frame.grid_columnconfigure(1, weight=1)
    pushing_frame.grid_columnconfigure(2, weight=1)
    print(main_frame.grid_size())
    pushing_frame.grid(row=2, column=1, sticky="E")


    leeway_frame = tk.Frame(main_frame, width=(frame_width - 100) / 3, height=400, bg="white")
    leeway_frame.config(borderwidth=6, relief="groove")

    leeway_frame.grid_rowconfigure(0, weight=1)
    leeway_frame.grid_rowconfigure(1, weight=1)
    leeway_frame.grid_rowconfigure(2, weight=1)
    leeway_frame.grid_columnconfigure(0, weight=1)
    leeway_frame.grid_columnconfigure(1, weight=1)
    leeway_frame.grid_columnconfigure(2, weight=1)

    leeway_frame.grid(row=1, column=1, sticky="N")
    # leeway_frame.place(relx=0.5, rely=0.5, anchor="center")
    print(leeway_frame.grid_size())

    emergency_frame = tk.Frame(main_frame, width=(frame_width - 100) / 3, height=400, bg="white")
    emergency_frame.config(borderwidth=6, relief="groove")

    emergency_frame.grid_rowconfigure(0, weight=1)
    emergency_frame.grid_rowconfigure(1, weight=1)
    emergency_frame.grid_rowconfigure(2, weight=1)
    emergency_frame.grid_columnconfigure(0, weight=1)
    emergency_frame.grid_columnconfigure(1, weight=1)
    emergency_frame.grid_columnconfigure(2, weight=1)

    emergency_frame.grid(row=1, column=2, sticky="W")
    # emergency_frame.place(relx=0.83, rely=0.5, anchor="center")

    Button_Pushing_img = tk.PhotoImage(file="images/Pushing_look.png")
    Button_Leeway_img = tk.PhotoImage(file="images/Leaway_look.png")
    Button_Emergency_img = tk.PhotoImage(file="images/Emergency_look.png")

    ######   First button for Pushing scenario  ######
    pushing_command = partial(do_the_scenario, pushing_frame, leeway_frame, emergency_frame, "pushing", main_frame,
                              root)
    pushing_btn = tk.Button(pushing_frame, image=Button_Pushing_img, anchor="c", command=pushing_command,
                            relief="raised")
    # pushing_btn.place(relx=0.5, rely=0.03, anchor="n")
    pushing_btn.grid(row=0, column=0, sticky="S")

    ######   Seccond button for Leeway scenario  ######
    leeway_command = partial(do_the_scenario, pushing_frame, leeway_frame, emergency_frame, "leeway", main_frame, root)
    leeway_btn = tk.Button(leeway_frame, image=Button_Leeway_img, anchor="c", command=leeway_command,
                           relief="raised")
    # leeway_btn.place(relx=0.5, rely=0.03, anchor="n")
    leeway_btn.grid(row=0, column=0, sticky="S")

    ######   Third button for Emergency Scenario  ######
    emergency_command = partial(do_the_scenario, pushing_frame, leeway_frame, emergency_frame, "emergency", main_frame,
                                root)
    emergency_btn = tk.Button(emergency_frame, image=Button_Emergency_img, anchor="c", command=emergency_command,
                              relief="raised")
    emergency_btn.grid(row=0, column=0, sticky="S")
    # emergency_btn.place(relx=0.5, rely=0.03, anchor="n")

    ######   the image for pushing scenario   ######
    opend_img_1 = Image.open("images/pushing.png")
    resize_image_1 = resize_image(opend_img_1, root)
    image_1 = ImageTk.PhotoImage(resize_image_1)
    img_1_lbl = tk.Label(pushing_frame, image=image_1)
    img_1_lbl.grid(row=0, column=0, sticky="N")
    # img_1_lbl.place(relx=0.5, rely=0.45, anchor="center")

    ######   the image for leeway scenario   ######
    opened_img_2 = Image.open("images/leeway.png")
    resize_image_2 = resize_image(opened_img_2, root)
    image_2 = ImageTk.PhotoImage(resize_image_2)
    img_2_lbl = tk.Label(leeway_frame, image=image_2)
    img_2_lbl.grid(row=0, column=0, sticky="N")
    # img_2_lbl.place(relx=0.5, rely=0.45, anchor="center")

    ######   the image for emergency scenario   ######
    opened_img_3 = Image.open("images/emergency.png")
    resize_image_3 = resize_image(opened_img_3, root)
    image_3 = ImageTk.PhotoImage(resize_image_3)
    img_3_lbl = tk.Label(emergency_frame, image=image_3)
    img_3_lbl.grid(row=0, column=0, sticky="N")
    # img_3_lbl.place(relx=0.5, rely=0.45, anchor="center")

    ######   The frames for descriptions   ######
    dsc_frame_sce_1 = tk.Frame(pushing_frame, width=350, height=((frame_width - 30) / 3) * 0.25, bg="white")
    dsc_frame_sce_1.grid(row=0, column=0, sticky="S")
    # dsc_frame_sce_1.place(relx=0.55, rely=0.85, anchor="center")
    dsc_frame_sce_1.config(borderwidth=2, relief="groove")

    dsc_frame_sce_2 = tk.Frame(leeway_frame, width=350, height=((frame_width - 30) / 3) * 0.25, bg="white")
    dsc_frame_sce_2.grid(row=0, column=0, sticky="S")
    # dsc_frame_sce_2.place(relx=0.55, rely=0.85, anchor="center")
    dsc_frame_sce_2.config(borderwidth=2, relief="groove")

    dsc_frame_sce_3 = tk.Frame(emergency_frame, width=350, height=((frame_width - 30) / 3) * 0.25, bg="white")
    dsc_frame_sce_3.grid(row=0, column=0, sticky="S")
    # dsc_frame_sce_3.place(relx=0.55, rely=0.85, anchor="center")
    dsc_frame_sce_3.config(borderwidth=2, relief="groove")

    ######   The description for pushing scenario   ######
    # label = BLabel(dsc_frame_sce_1)
    # label.add_option("Objective: Clear the encroaching pack ice from the indicated area using the pushing technique")
    # label.add_option("Time: 15min")
    # label.add_option("Vessel heading: 120deg")
    # label.add_option("Current: 0.4kn")
    # label.add_option("Current direction: 180deg S")
    # label.add_option("Wind: Light")
    # label.add_option("Ice: 0.3-0.7m first year ice, 4-tenths concentration")
    # label.l.place(relx=0.5, rely=0.5, anchor="center")
    llbb = tk.Label(dsc_frame_sce_1,
                    text="Objective: Clear the indicated area aft of\n\tmidships using the leeway technique\n Time: 15min\nVessel heading: 60deg\nTarget heading: 0deg!\nCurrent: 1kn",
                    bg="white", justify="left")
    llbb.grid(row=0, column=0, sticky="S")
    # llbb.place(relx=0.5, rely=0.5, anchor="center")

    ######   The description for leeway scenario   ######
    label = BLabel(dsc_frame_sce_2)
    label.add_option("Objective: Clear the indicated area aft of midships using the leeway technique")
    label.add_option("Time: 15min")
    label.add_option("Vessel heading: 60deg")
    label.add_option("Target heading: 0deg!")
    label.add_option("Current: 1kn")
    label.add_option("Current direction: 180deg S")
    label.add_option("Wind: Light")
    label.add_option("Ice: 0.3-0.7m first year ice, 5-tenths concentration")
    # label.l.place(relx=0.5, rely=0.5, anchor="center")

    ######   The description for emergency scenario   ######
    label = BLabel(dsc_frame_sce_3)
    label.add_option("Objective: Clear encroaching pack ice from the boxed area shown")
    label.add_option("Time: 30min")
    label.add_option("Current: 0.5kn")
    label.add_option("Current direction: 180deg S")
    label.add_option("Wind: Light")
    label.add_option("Ice: 0.3-0.7m first year ice")
    # label.l.place(relx=0.5, rely=0.5, anchor="center")
    root.mainloop()

    {"lat_top_left": 60.51116,
     "long_top_left": 146.35677,
     "lat_top_right": 60.51116,
     "long_top_right": 146.35300,
     "lat_btm_left": 60.50930,
     "long_btm_left": 146.35677,
     "lat_btm_right": 60.50930,
     "long_btm_right": 146.35300, "center_trgt_lat": 60.51023040,
     "center_trgt_long": 146.35488790}

    {"lat_top_left": 60.51117,
     "long_top_left": 146.35678,
     "lat_top_right": 60.51117,
     "long_top_right": 146.35299,
     "lat_btm_left": 60.50930,
     "long_btm_left": 146.35678,
     "lat_btm_right": 60.50930,
     "long_btm_right": 146.35299},