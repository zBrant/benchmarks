TUNE=base
LABEL=primeiro-teste-m64
NUMBER=526
NAME=blender_r
SOURCES= blender/source/creator/creator.c \
	 blender/source/blender/windowmanager/intern/wm.c \
	 blender/source/blender/windowmanager/intern/wm_playanim.c \
	 blender/source/blender/windowmanager/intern/wm_cursors.c \
	 blender/source/blender/windowmanager/intern/wm_dragdrop.c \
	 blender/source/blender/windowmanager/intern/wm_draw.c \
	 blender/source/blender/windowmanager/intern/wm_event_system.c \
	 blender/source/blender/windowmanager/intern/wm_files.c \
	 blender/source/blender/windowmanager/intern/wm_gesture.c \
	 blender/source/blender/windowmanager/intern/wm_init_exit.c \
	 blender/source/blender/windowmanager/intern/wm_jobs.c \
	 blender/source/blender/windowmanager/intern/wm_keymap.c \
	 blender/source/blender/windowmanager/intern/wm_operators.c \
	 blender/source/blender/windowmanager/intern/wm_subwindow.c \
	 blender/source/blender/windowmanager/intern/wm_window.c \
	 blender/source/blender/editors/space_api/spacetypes.c \
	 blender/source/blender/editors/space_action/action_draw.c \
	 blender/source/blender/editors/space_action/action_edit.c \
	 blender/source/blender/editors/space_action/action_ops.c \
	 blender/source/blender/editors/space_action/action_select.c \
	 blender/source/blender/editors/space_action/space_action.c \
	 blender/source/blender/editors/space_buttons/buttons_context.c \
	 blender/source/blender/editors/space_buttons/buttons_ops.c \
	 blender/source/blender/editors/space_buttons/buttons_texture.c \
	 blender/source/blender/editors/space_buttons/space_buttons.c \
	 blender/source/blender/editors/space_console/console_draw.c \
	 blender/source/blender/editors/space_console/console_ops.c \
	 blender/source/blender/editors/space_console/space_console.c \
	 blender/source/blender/editors/space_file/file_draw.c \
	 blender/source/blender/editors/space_file/file_ops.c \
	 blender/source/blender/editors/space_file/file_panels.c \
	 blender/source/blender/editors/space_file/filelist.c \
	 blender/source/blender/editors/space_file/filesel.c \
	 blender/source/blender/editors/space_file/fsmenu.c \
	 blender/source/blender/editors/space_file/space_file.c \
	 blender/source/blender/editors/space_graph/graph_buttons.c \
	 blender/source/blender/editors/space_graph/graph_draw.c \
	 blender/source/blender/editors/space_graph/graph_edit.c \
	 blender/source/blender/editors/space_graph/graph_ops.c \
	 blender/source/blender/editors/space_graph/graph_select.c \
	 blender/source/blender/editors/space_graph/graph_utils.c \
	 blender/source/blender/editors/space_graph/space_graph.c \
	 blender/source/blender/editors/space_image/image_buttons.c \
	 blender/source/blender/editors/space_image/image_draw.c \
	 blender/source/blender/editors/space_image/image_edit.c \
	 blender/source/blender/editors/space_image/image_ops.c \
	 blender/source/blender/editors/space_image/space_image.c \
	 blender/source/blender/editors/space_info/info_ops.c \
	 blender/source/blender/editors/space_info/info_stats.c \
	 blender/source/blender/editors/space_info/info_draw.c \
	 blender/source/blender/editors/space_info/info_report.c \
	 blender/source/blender/editors/space_info/textview.c \
	 blender/source/blender/editors/space_info/space_info.c \
	 blender/source/blender/editors/space_logic/logic_buttons.c \
	 blender/source/blender/editors/space_logic/logic_ops.c \
	 blender/source/blender/editors/space_logic/logic_window.c \
	 blender/source/blender/editors/space_logic/space_logic.c \
	 blender/source/blender/editors/space_nla/nla_buttons.c \
	 blender/source/blender/editors/space_nla/nla_channels.c \
	 blender/source/blender/editors/space_nla/nla_draw.c \
	 blender/source/blender/editors/space_nla/nla_edit.c \
	 blender/source/blender/editors/space_nla/nla_ops.c \
	 blender/source/blender/editors/space_nla/nla_select.c \
	 blender/source/blender/editors/space_nla/space_nla.c \
	 blender/source/blender/editors/space_node/drawnode.c \
	 blender/source/blender/editors/space_node/node_add.c \
	 blender/source/blender/editors/space_node/node_buttons.c \
	 blender/source/blender/editors/space_node/node_draw.c \
	 blender/source/blender/editors/space_node/node_edit.c \
	 blender/source/blender/editors/space_node/node_group.c \
	 blender/source/blender/editors/space_node/node_ops.c \
	 blender/source/blender/editors/space_node/node_relationships.c \
	 blender/source/blender/editors/space_node/node_select.c \
	 blender/source/blender/editors/space_node/node_templates.c \
	 blender/source/blender/editors/space_node/node_toolbar.c \
	 blender/source/blender/editors/space_node/node_view.c \
	 blender/source/blender/editors/space_node/space_node.c \
	 blender/source/blender/editors/space_outliner/outliner_draw.c \
	 blender/source/blender/editors/space_outliner/outliner_edit.c \
	 blender/source/blender/editors/space_outliner/outliner_ops.c \
	 blender/source/blender/editors/space_outliner/outliner_select.c \
	 blender/source/blender/editors/space_outliner/outliner_tools.c \
	 blender/source/blender/editors/space_outliner/outliner_tree.c \
	 blender/source/blender/editors/space_outliner/space_outliner.c \
	 blender/source/blender/editors/space_script/script_edit.c \
	 blender/source/blender/editors/space_script/script_ops.c \
	 blender/source/blender/editors/space_script/space_script.c \
	 blender/source/blender/editors/space_sequencer/sequencer_add.c \
	 blender/source/blender/editors/space_sequencer/sequencer_buttons.c \
	 blender/source/blender/editors/space_sequencer/sequencer_draw.c \
	 blender/source/blender/editors/space_sequencer/sequencer_edit.c \
	 blender/source/blender/editors/space_sequencer/sequencer_modifier.c \
	 blender/source/blender/editors/space_sequencer/sequencer_ops.c \
	 blender/source/blender/editors/space_sequencer/sequencer_scopes.c \
	 blender/source/blender/editors/space_sequencer/sequencer_select.c \
	 blender/source/blender/editors/space_sequencer/sequencer_view.c \
	 blender/source/blender/editors/space_sequencer/space_sequencer.c \
	 blender/source/blender/editors/space_text/space_text.c \
	 blender/source/blender/editors/space_text/text_autocomplete.c \
	 blender/source/blender/editors/space_text/text_draw.c \
	 blender/source/blender/editors/space_text/text_format.c \
	 blender/source/blender/editors/space_text/text_format_lua.c \
	 blender/source/blender/editors/space_text/text_format_osl.c \
	 blender/source/blender/editors/space_text/text_format_py.c \
	 blender/source/blender/editors/space_text/text_header.c \
	 blender/source/blender/editors/space_text/text_ops.c \
	 blender/source/blender/editors/space_time/space_time.c \
	 blender/source/blender/editors/space_time/time_ops.c \
	 blender/source/blender/editors/space_userpref/space_userpref.c \
	 blender/source/blender/editors/space_userpref/userpref_ops.c \
	 blender/source/blender/editors/space_view3d/drawanimviz.c \
	 blender/source/blender/editors/space_view3d/drawarmature.c \
	 blender/source/blender/editors/space_view3d/drawmesh.c \
	 blender/source/blender/editors/space_view3d/drawobject.c \
	 blender/source/blender/editors/space_view3d/drawvolume.c \
	 blender/source/blender/editors/space_view3d/space_view3d.c \
	 blender/source/blender/editors/space_view3d/view3d_buttons.c \
	 blender/source/blender/editors/space_view3d/view3d_camera_control.c \
	 blender/source/blender/editors/space_view3d/view3d_draw.c \
	 blender/source/blender/editors/space_view3d/view3d_edit.c \
	 blender/source/blender/editors/space_view3d/view3d_fly.c \
	 blender/source/blender/editors/space_view3d/view3d_walk.c \
	 blender/source/blender/editors/space_view3d/view3d_header.c \
	 blender/source/blender/editors/space_view3d/view3d_iterators.c \
	 blender/source/blender/editors/space_view3d/view3d_ops.c \
	 blender/source/blender/editors/space_view3d/view3d_project.c \
	 blender/source/blender/editors/space_view3d/view3d_ruler.c \
	 blender/source/blender/editors/space_view3d/view3d_select.c \
	 blender/source/blender/editors/space_view3d/view3d_snap.c \
	 blender/source/blender/editors/space_view3d/view3d_toolbar.c \
	 blender/source/blender/editors/space_view3d/view3d_view.c \
	 blender/source/blender/editors/space_clip/clip_buttons.c \
	 blender/source/blender/editors/space_clip/clip_dopesheet_draw.c \
	 blender/source/blender/editors/space_clip/clip_dopesheet_ops.c \
	 blender/source/blender/editors/space_clip/clip_draw.c \
	 blender/source/blender/editors/space_clip/clip_editor.c \
	 blender/source/blender/editors/space_clip/clip_graph_draw.c \
	 blender/source/blender/editors/space_clip/clip_graph_ops.c \
	 blender/source/blender/editors/space_clip/clip_ops.c \
	 blender/source/blender/editors/space_clip/clip_toolbar.c \
	 blender/source/blender/editors/space_clip/clip_utils.c \
	 blender/source/blender/editors/space_clip/space_clip.c \
	 blender/source/blender/editors/space_clip/tracking_ops.c \
	 blender/source/blender/editors/space_clip/tracking_select.c \
	 blender/source/blender/editors/transform/transform.c \
	 blender/source/blender/editors/transform/transform_constraints.c \
	 blender/source/blender/editors/transform/transform_conversions.c \
	 blender/source/blender/editors/transform/transform_generics.c \
	 blender/source/blender/editors/transform/transform_input.c \
	 blender/source/blender/editors/transform/transform_manipulator.c \
	 blender/source/blender/editors/transform/transform_ops.c \
	 blender/source/blender/editors/transform/transform_orientations.c \
	 blender/source/blender/editors/transform/transform_snap.c \
	 blender/source/blender/editors/util/ed_transverts.c \
	 blender/source/blender/editors/util/ed_util.c \
	 blender/source/blender/editors/util/editmode_undo.c \
	 blender/source/blender/editors/util/numinput.c \
	 blender/source/blender/editors/util/undo.c \
	 blender/source/blender/editors/uvedit/uvedit_buttons.c \
	 blender/source/blender/editors/uvedit/uvedit_draw.c \
	 blender/source/blender/editors/uvedit/uvedit_ops.c \
	 blender/source/blender/editors/uvedit/uvedit_parametrizer.c \
	 blender/source/blender/editors/uvedit/uvedit_smart_stitch.c \
	 blender/source/blender/editors/uvedit/uvedit_unwrap_ops.c \
	 blender/source/blender/editors/curve/curve_ops.c \
	 blender/source/blender/editors/curve/editcurve.c \
	 blender/source/blender/editors/curve/editcurve_add.c \
	 blender/source/blender/editors/curve/editfont.c \
	 blender/source/blender/editors/curve/lorem.c \
	 blender/source/blender/editors/gpencil/drawgpencil.c \
	 blender/source/blender/editors/gpencil/editaction_gpencil.c \
	 blender/source/blender/editors/gpencil/gpencil_buttons.c \
	 blender/source/blender/editors/gpencil/gpencil_edit.c \
	 blender/source/blender/editors/gpencil/gpencil_ops.c \
	 blender/source/blender/editors/gpencil/gpencil_paint.c \
	 blender/source/blender/editors/gpencil/gpencil_undo.c \
	 blender/source/blender/editors/interface/interface.c \
	 blender/source/blender/editors/interface/interface_anim.c \
	 blender/source/blender/editors/interface/interface_draw.c \
	 blender/source/blender/editors/interface/interface_eyedropper.c \
	 blender/source/blender/editors/interface/interface_handlers.c \
	 blender/source/blender/editors/interface/interface_icons.c \
	 blender/source/blender/editors/interface/interface_layout.c \
	 blender/source/blender/editors/interface/interface_ops.c \
	 blender/source/blender/editors/interface/interface_panel.c \
	 blender/source/blender/editors/interface/interface_regions.c \
	 blender/source/blender/editors/interface/interface_style.c \
	 blender/source/blender/editors/interface/interface_templates.c \
	 blender/source/blender/editors/interface/interface_utils.c \
	 blender/source/blender/editors/interface/interface_widgets.c \
	 blender/source/blender/editors/interface/resources.c \
	 blender/source/blender/editors/interface/view2d.c \
	 blender/source/blender/editors/interface/view2d_ops.c \
	 blender/source/blender/editors/mesh/editface.c \
	 blender/source/blender/editors/mesh/editmesh_add.c \
	 blender/source/blender/editors/mesh/editmesh_bevel.c \
	 blender/source/blender/editors/mesh/editmesh_bisect.c \
	 blender/source/blender/editors/mesh/editmesh_extrude.c \
	 blender/source/blender/editors/mesh/editmesh_inset.c \
	 blender/source/blender/editors/mesh/editmesh_intersect.c \
	 blender/source/blender/editors/mesh/editmesh_knife.c \
	 blender/source/blender/editors/mesh/editmesh_knife_project.c \
	 blender/source/blender/editors/mesh/editmesh_loopcut.c \
	 blender/source/blender/editors/mesh/editmesh_path.c \
	 blender/source/blender/editors/mesh/editmesh_rip.c \
	 blender/source/blender/editors/mesh/editmesh_rip_edge.c \
	 blender/source/blender/editors/mesh/editmesh_select.c \
	 blender/source/blender/editors/mesh/editmesh_tools.c \
	 blender/source/blender/editors/mesh/editmesh_utils.c \
	 blender/source/blender/editors/mesh/mesh_data.c \
	 blender/source/blender/editors/mesh/mesh_ops.c \
	 blender/source/blender/editors/mesh/meshtools.c \
	 blender/source/blender/editors/metaball/mball_edit.c \
	 blender/source/blender/editors/metaball/mball_ops.c \
	 blender/source/blender/editors/object/object_add.c \
	 blender/source/blender/editors/object/object_bake.c \
	 blender/source/blender/editors/object/object_bake_api.c \
	 blender/source/blender/editors/object/object_constraint.c \
	 blender/source/blender/editors/object/object_edit.c \
	 blender/source/blender/editors/object/object_group.c \
	 blender/source/blender/editors/object/object_hook.c \
	 blender/source/blender/editors/object/object_lattice.c \
	 blender/source/blender/editors/object/object_lod.c \
	 blender/source/blender/editors/object/object_modifier.c \
	 blender/source/blender/editors/object/object_ops.c \
	 blender/source/blender/editors/object/object_random.c \
	 blender/source/blender/editors/object/object_relations.c \
	 blender/source/blender/editors/object/object_select.c \
	 blender/source/blender/editors/object/object_shapekey.c \
	 blender/source/blender/editors/object/object_transform.c \
	 blender/source/blender/editors/object/object_warp.c \
	 blender/source/blender/editors/object/object_vgroup.c \
	 blender/source/blender/editors/armature/armature_add.c \
	 blender/source/blender/editors/armature/armature_edit.c \
	 blender/source/blender/editors/armature/armature_naming.c \
	 blender/source/blender/editors/armature/armature_ops.c \
	 blender/source/blender/editors/armature/armature_relations.c \
	 blender/source/blender/editors/armature/armature_select.c \
	 blender/source/blender/editors/armature/armature_skinning.c \
	 blender/source/blender/editors/armature/armature_utils.c \
	 blender/source/blender/editors/armature/editarmature_generate.c \
	 blender/source/blender/editors/armature/editarmature_retarget.c \
	 blender/source/blender/editors/armature/editarmature_sketch.c \
	 blender/source/blender/editors/armature/meshlaplacian.c \
	 blender/source/blender/editors/armature/pose_edit.c \
	 blender/source/blender/editors/armature/pose_lib.c \
	 blender/source/blender/editors/armature/pose_group.c \
	 blender/source/blender/editors/armature/pose_select.c \
	 blender/source/blender/editors/armature/pose_slide.c \
	 blender/source/blender/editors/armature/pose_transform.c \
	 blender/source/blender/editors/armature/pose_utils.c \
	 blender/source/blender/editors/armature/reeb.c \
	 blender/source/blender/editors/physics/dynamicpaint_ops.c \
	 blender/source/blender/editors/physics/particle_boids.c \
	 blender/source/blender/editors/physics/particle_edit.c \
	 blender/source/blender/editors/physics/particle_object.c \
	 blender/source/blender/editors/physics/physics_fluid.c \
	 blender/source/blender/editors/physics/physics_ops.c \
	 blender/source/blender/editors/physics/physics_pointcache.c \
	 blender/source/blender/editors/physics/rigidbody_constraint.c \
	 blender/source/blender/editors/physics/rigidbody_object.c \
	 blender/source/blender/editors/physics/rigidbody_world.c \
	 blender/source/blender/editors/render/render_internal.c \
	 blender/source/blender/editors/render/render_opengl.c \
	 blender/source/blender/editors/render/render_ops.c \
	 blender/source/blender/editors/render/render_preview.c \
	 blender/source/blender/editors/render/render_shading.c \
	 blender/source/blender/editors/render/render_update.c \
	 blender/source/blender/editors/render/render_view.c \
	 blender/source/blender/editors/screen/area.c \
	 blender/source/blender/editors/screen/glutil.c \
	 blender/source/blender/editors/screen/screen_context.c \
	 blender/source/blender/editors/screen/screen_edit.c \
	 blender/source/blender/editors/screen/screen_ops.c \
	 blender/source/blender/editors/screen/screendump.c \
	 blender/source/blender/editors/sculpt_paint/paint_cursor.c \
	 blender/source/blender/editors/sculpt_paint/paint_curve.c \
	 blender/source/blender/editors/sculpt_paint/paint_hide.c \
	 blender/source/blender/editors/sculpt_paint/paint_image.c \
	 blender/source/blender/editors/sculpt_paint/paint_image_2d.c \
	 blender/source/blender/editors/sculpt_paint/paint_image_proj.c \
	 blender/source/blender/editors/sculpt_paint/paint_mask.c \
	 blender/source/blender/editors/sculpt_paint/paint_ops.c \
	 blender/source/blender/editors/sculpt_paint/paint_stroke.c \
	 blender/source/blender/editors/sculpt_paint/paint_undo.c \
	 blender/source/blender/editors/sculpt_paint/paint_utils.c \
	 blender/source/blender/editors/sculpt_paint/paint_vertex.c \
	 blender/source/blender/editors/sculpt_paint/paint_vertex_proj.c \
	 blender/source/blender/editors/sculpt_paint/sculpt.c \
	 blender/source/blender/editors/sculpt_paint/sculpt_undo.c \
	 blender/source/blender/editors/sculpt_paint/sculpt_uv.c \
	 blender/source/blender/editors/sound/sound_ops.c \
	 blender/source/blender/editors/animation/anim_channels_defines.c \
	 blender/source/blender/editors/animation/anim_channels_edit.c \
	 blender/source/blender/editors/animation/anim_deps.c \
	 blender/source/blender/editors/animation/anim_draw.c \
	 blender/source/blender/editors/animation/anim_filter.c \
	 blender/source/blender/editors/animation/anim_ipo_utils.c \
	 blender/source/blender/editors/animation/anim_markers.c \
	 blender/source/blender/editors/animation/anim_ops.c \
	 blender/source/blender/editors/animation/drivers.c \
	 blender/source/blender/editors/animation/fmodifier_ui.c \
	 blender/source/blender/editors/animation/keyframes_draw.c \
	 blender/source/blender/editors/animation/keyframes_edit.c \
	 blender/source/blender/editors/animation/keyframes_general.c \
	 blender/source/blender/editors/animation/keyframing.c \
	 blender/source/blender/editors/animation/keyingsets.c \
	 blender_bin/release/datafiles/bfont.pfb.c \
	 blender_bin/release/datafiles/bfont.ttf.c \
	 blender_bin/release/datafiles/bmonofont.ttf.c \
	 blender_bin/release/datafiles/startup.blend.c \
	 blender/source/blender/editors/mask/mask_add.c \
	 blender/source/blender/editors/mask/mask_draw.c \
	 blender/source/blender/editors/mask/mask_edit.c \
	 blender/source/blender/editors/mask/mask_editaction.c \
	 blender/source/blender/editors/mask/mask_ops.c \
	 blender/source/blender/editors/mask/mask_relationships.c \
	 blender/source/blender/editors/mask/mask_select.c \
	 blender/source/blender/editors/mask/mask_shapekey.c \
	 blender/source/blender/editors/io/io_ops.c \
	 blender/source/blender/render/intern/raytrace/rayobject.cpp \
	 blender/source/blender/render/intern/raytrace/rayobject_empty.cpp \
	 blender/source/blender/render/intern/raytrace/rayobject_octree.cpp \
	 blender/source/blender/render/intern/raytrace/rayobject_raycounter.cpp \
	 blender/source/blender/render/intern/raytrace/rayobject_svbvh.cpp \
	 blender/source/blender/render/intern/raytrace/rayobject_instance.cpp \
	 blender/source/blender/render/intern/raytrace/rayobject_qbvh.cpp \
	 blender/source/blender/render/intern/raytrace/rayobject_rtbuild.cpp \
	 blender/source/blender/render/intern/raytrace/rayobject_vbvh.cpp \
	 blender/source/blender/render/intern/source/bake.c \
	 blender/source/blender/render/intern/source/bake_api.c \
	 blender/source/blender/render/intern/source/convertblender.c \
	 blender/source/blender/render/intern/source/envmap.c \
	 blender/source/blender/render/intern/source/external_engine.c \
	 blender/source/blender/render/intern/source/imagetexture.c \
	 blender/source/blender/render/intern/source/initrender.c \
	 blender/source/blender/render/intern/source/multires_bake.c \
	 blender/source/blender/render/intern/source/occlusion.c \
	 blender/source/blender/render/intern/source/pipeline.c \
	 blender/source/blender/render/intern/source/pixelblending.c \
	 blender/source/blender/render/intern/source/pixelshading.c \
	 blender/source/blender/render/intern/source/pointdensity.c \
	 blender/source/blender/render/intern/source/rayshade.c \
	 blender/source/blender/render/intern/source/rendercore.c \
	 blender/source/blender/render/intern/source/render_result.c \
	 blender/source/blender/render/intern/source/render_texture.c \
	 blender/source/blender/render/intern/source/renderdatabase.c \
	 blender/source/blender/render/intern/source/shadbuf.c \
	 blender/source/blender/render/intern/source/shadeinput.c \
	 blender/source/blender/render/intern/source/shadeoutput.c \
	 blender/source/blender/render/intern/source/sss.c \
	 blender/source/blender/render/intern/source/strand.c \
	 blender/source/blender/render/intern/source/sunsky.c \
	 blender/source/blender/render/intern/source/texture_ocean.c \
	 blender/source/blender/render/intern/source/volume_precache.c \
	 blender/source/blender/render/intern/source/volumetric.c \
	 blender/source/blender/render/intern/source/voxeldata.c \
	 blender/source/blender/render/intern/source/zbuf.c \
	 blender/source/blender/ikplugin/intern/ikplugin_api.c \
	 blender/source/blender/modifiers/intern/MOD_armature.c \
	 blender/source/blender/modifiers/intern/MOD_array.c \
	 blender/source/blender/modifiers/intern/MOD_bevel.c \
	 blender/source/blender/modifiers/intern/MOD_boolean.c \
	 blender/source/blender/modifiers/intern/MOD_build.c \
	 blender/source/blender/modifiers/intern/MOD_cast.c \
	 blender/source/blender/modifiers/intern/MOD_cloth.c \
	 blender/source/blender/modifiers/intern/MOD_collision.c \
	 blender/source/blender/modifiers/intern/MOD_curve.c \
	 blender/source/blender/modifiers/intern/MOD_decimate.c \
	 blender/source/blender/modifiers/intern/MOD_displace.c \
	 blender/source/blender/modifiers/intern/MOD_dynamicpaint.c \
	 blender/source/blender/modifiers/intern/MOD_edgesplit.c \
	 blender/source/blender/modifiers/intern/MOD_explode.c \
	 blender/source/blender/modifiers/intern/MOD_fluidsim.c \
	 blender/source/blender/modifiers/intern/MOD_fluidsim_util.c \
	 blender/source/blender/modifiers/intern/MOD_hook.c \
	 blender/source/blender/modifiers/intern/MOD_laplaciandeform.c \
	 blender/source/blender/modifiers/intern/MOD_laplaciansmooth.c \
	 blender/source/blender/modifiers/intern/MOD_lattice.c \
	 blender/source/blender/modifiers/intern/MOD_mask.c \
	 blender/source/blender/modifiers/intern/MOD_meshcache.c \
	 blender/source/blender/modifiers/intern/MOD_meshcache_mdd.c \
	 blender/source/blender/modifiers/intern/MOD_meshcache_pc2.c \
	 blender/source/blender/modifiers/intern/MOD_meshcache_util.c \
	 blender/source/blender/modifiers/intern/MOD_meshdeform.c \
	 blender/source/blender/modifiers/intern/MOD_mirror.c \
	 blender/source/blender/modifiers/intern/MOD_multires.c \
	 blender/source/blender/modifiers/intern/MOD_none.c \
	 blender/source/blender/modifiers/intern/MOD_ocean.c \
	 blender/source/blender/modifiers/intern/MOD_particleinstance.c \
	 blender/source/blender/modifiers/intern/MOD_particlesystem.c \
	 blender/source/blender/modifiers/intern/MOD_remesh.c \
	 blender/source/blender/modifiers/intern/MOD_screw.c \
	 blender/source/blender/modifiers/intern/MOD_shapekey.c \
	 blender/source/blender/modifiers/intern/MOD_shrinkwrap.c \
	 blender/source/blender/modifiers/intern/MOD_simpledeform.c \
	 blender/source/blender/modifiers/intern/MOD_skin.c \
	 blender/source/blender/modifiers/intern/MOD_smoke.c \
	 blender/source/blender/modifiers/intern/MOD_smooth.c \
	 blender/source/blender/modifiers/intern/MOD_softbody.c \
	 blender/source/blender/modifiers/intern/MOD_solidify.c \
	 blender/source/blender/modifiers/intern/MOD_subsurf.c \
	 blender/source/blender/modifiers/intern/MOD_surface.c \
	 blender/source/blender/modifiers/intern/MOD_triangulate.c \
	 blender/source/blender/modifiers/intern/MOD_util.c \
	 blender/source/blender/modifiers/intern/MOD_uvwarp.c \
	 blender/source/blender/modifiers/intern/MOD_uvproject.c \
	 blender/source/blender/modifiers/intern/MOD_warp.c \
	 blender/source/blender/modifiers/intern/MOD_wave.c \
	 blender/source/blender/modifiers/intern/MOD_weightvg_util.c \
	 blender/source/blender/modifiers/intern/MOD_weightvgedit.c \
	 blender/source/blender/modifiers/intern/MOD_weightvgmix.c \
	 blender/source/blender/modifiers/intern/MOD_weightvgproximity.c \
	 blender/source/blender/modifiers/intern/MOD_wireframe.c \
	 blender/source/blender/bmesh/operators/bmo_beautify.c \
	 blender/source/blender/bmesh/operators/bmo_bevel.c \
	 blender/source/blender/bmesh/operators/bmo_bisect_plane.c \
	 blender/source/blender/bmesh/operators/bmo_bridge.c \
	 blender/source/blender/bmesh/operators/bmo_connect.c \
	 blender/source/blender/bmesh/operators/bmo_connect_nonplanar.c \
	 blender/source/blender/bmesh/operators/bmo_connect_pair.c \
	 blender/source/blender/bmesh/operators/bmo_create.c \
	 blender/source/blender/bmesh/operators/bmo_dissolve.c \
	 blender/source/blender/bmesh/operators/bmo_dupe.c \
	 blender/source/blender/bmesh/operators/bmo_edgenet.c \
	 blender/source/blender/bmesh/operators/bmo_extrude.c \
	 blender/source/blender/bmesh/operators/bmo_fill_attribute.c \
	 blender/source/blender/bmesh/operators/bmo_fill_edgeloop.c \
	 blender/source/blender/bmesh/operators/bmo_fill_grid.c \
	 blender/source/blender/bmesh/operators/bmo_fill_holes.c \
	 blender/source/blender/bmesh/operators/bmo_inset.c \
	 blender/source/blender/bmesh/operators/bmo_join_triangles.c \
	 blender/source/blender/bmesh/operators/bmo_mesh_conv.c \
	 blender/source/blender/bmesh/operators/bmo_mirror.c \
	 blender/source/blender/bmesh/operators/bmo_normals.c \
	 blender/source/blender/bmesh/operators/bmo_poke.c \
	 blender/source/blender/bmesh/operators/bmo_primitive.c \
	 blender/source/blender/bmesh/operators/bmo_removedoubles.c \
	 blender/source/blender/bmesh/operators/bmo_similar.c \
	 blender/source/blender/bmesh/operators/bmo_smooth_laplacian.c \
	 blender/source/blender/bmesh/operators/bmo_split_edges.c \
	 blender/source/blender/bmesh/operators/bmo_subdivide.c \
	 blender/source/blender/bmesh/operators/bmo_subdivide_edgering.c \
	 blender/source/blender/bmesh/operators/bmo_symmetrize.c \
	 blender/source/blender/bmesh/operators/bmo_triangulate.c \
	 blender/source/blender/bmesh/operators/bmo_unsubdivide.c \
	 blender/source/blender/bmesh/operators/bmo_utils.c \
	 blender/source/blender/bmesh/operators/bmo_wireframe.c \
	 blender/source/blender/bmesh/intern/bmesh_construct.c \
	 blender/source/blender/bmesh/intern/bmesh_core.c \
	 blender/source/blender/bmesh/intern/bmesh_edgeloop.c \
	 blender/source/blender/bmesh/intern/bmesh_delete.c \
	 blender/source/blender/bmesh/intern/bmesh_interp.c \
	 blender/source/blender/bmesh/intern/bmesh_iterators.c \
	 blender/source/blender/bmesh/intern/bmesh_log.c \
	 blender/source/blender/bmesh/intern/bmesh_marking.c \
	 blender/source/blender/bmesh/intern/bmesh_mesh.c \
	 blender/source/blender/bmesh/intern/bmesh_mesh_conv.c \
	 blender/source/blender/bmesh/intern/bmesh_mods.c \
	 blender/source/blender/bmesh/intern/bmesh_opdefines.c \
	 blender/source/blender/bmesh/intern/bmesh_operators.c \
	 blender/source/blender/bmesh/intern/bmesh_polygon.c \
	 blender/source/blender/bmesh/intern/bmesh_queries.c \
	 blender/source/blender/bmesh/intern/bmesh_structure.c \
	 blender/source/blender/bmesh/intern/bmesh_walkers.c \
	 blender/source/blender/bmesh/intern/bmesh_walkers_impl.c \
	 blender/source/blender/bmesh/tools/bmesh_beautify.c \
	 blender/source/blender/bmesh/tools/bmesh_bevel.c \
	 blender/source/blender/bmesh/tools/bmesh_bisect_plane.c \
	 blender/source/blender/bmesh/tools/bmesh_decimate_collapse.c \
	 blender/source/blender/bmesh/tools/bmesh_decimate_dissolve.c \
	 blender/source/blender/bmesh/tools/bmesh_decimate_unsubdivide.c \
	 blender/source/blender/bmesh/tools/bmesh_edgenet.c \
	 blender/source/blender/bmesh/tools/bmesh_edgesplit.c \
	 blender/source/blender/bmesh/tools/bmesh_intersect.c \
	 blender/source/blender/bmesh/tools/bmesh_path.c \
	 blender/source/blender/bmesh/tools/bmesh_region_match.c \
	 blender/source/blender/bmesh/tools/bmesh_triangulate.c \
	 blender/source/blender/bmesh/tools/bmesh_wireframe.c \
	 blender/source/blender/blenkernel/intern/CCGSubSurf.c \
	 blender/source/blender/blenkernel/intern/DerivedMesh.c \
	 blender/source/blender/blenkernel/intern/action.c \
	 blender/source/blender/blenkernel/intern/addon.c \
	 blender/source/blender/blenkernel/intern/anim.c \
	 blender/source/blender/blenkernel/intern/anim_sys.c \
	 blender/source/blender/blenkernel/intern/armature.c \
	 blender/source/blender/blenkernel/intern/autoexec.c \
	 blender/source/blender/blenkernel/intern/blender.c \
	 blender/source/blender/blenkernel/intern/bmfont.c \
	 blender/source/blender/blenkernel/intern/boids.c \
	 blender/source/blender/blenkernel/intern/bpath.c \
	 blender/source/blender/blenkernel/intern/brush.c \
	 blender/source/blender/blenkernel/intern/bullet.c \
	 blender/source/blender/blenkernel/intern/bvhutils.c \
	 blender/source/blender/blenkernel/intern/camera.c \
	 blender/source/blender/blenkernel/intern/cdderivedmesh.c \
	 blender/source/blender/blenkernel/intern/cloth.c \
	 blender/source/blender/blenkernel/intern/collision.c \
	 blender/source/blender/blenkernel/intern/colortools.c \
	 blender/source/blender/blenkernel/intern/constraint.c \
	 blender/source/blender/blenkernel/intern/context.c \
	 blender/source/blender/blenkernel/intern/crazyspace.c \
	 blender/source/blender/blenkernel/intern/curve.c \
	 blender/source/blender/blenkernel/intern/customdata.c \
	 blender/source/blender/blenkernel/intern/customdata_file.c \
	 blender/source/blender/blenkernel/intern/deform.c \
	 blender/source/blender/blenkernel/intern/depsgraph.c \
	 blender/source/blender/blenkernel/intern/displist.c \
	 blender/source/blender/blenkernel/intern/dynamicpaint.c \
	 blender/source/blender/blenkernel/intern/editderivedmesh.c \
	 blender/source/blender/blenkernel/intern/editmesh.c \
	 blender/source/blender/blenkernel/intern/editmesh_bvh.c \
	 blender/source/blender/blenkernel/intern/effect.c \
	 blender/source/blender/blenkernel/intern/fcurve.c \
	 blender/source/blender/blenkernel/intern/fluidsim.c \
	 blender/source/blender/blenkernel/intern/fmodifier.c \
	 blender/source/blender/blenkernel/intern/font.c \
	 blender/source/blender/blenkernel/intern/freestyle.c \
	 blender/source/blender/blenkernel/intern/gpencil.c \
	 blender/source/blender/blenkernel/intern/group.c \
	 blender/source/blender/blenkernel/intern/icons.c \
	 blender/source/blender/blenkernel/intern/idcode.c \
	 blender/source/blender/blenkernel/intern/idprop.c \
	 blender/source/blender/blenkernel/intern/image.c \
	 blender/source/blender/blenkernel/intern/image_gen.c \
	 blender/source/blender/blenkernel/intern/implicit.c \
	 blender/source/blender/blenkernel/intern/ipo.c \
	 blender/source/blender/blenkernel/intern/key.c \
	 blender/source/blender/blenkernel/intern/lamp.c \
	 blender/source/blender/blenkernel/intern/lattice.c \
	 blender/source/blender/blenkernel/intern/library.c \
	 blender/source/blender/blenkernel/intern/library_query.c \
	 blender/source/blender/blenkernel/intern/linestyle.c \
	 blender/source/blender/blenkernel/intern/mask.c \
	 blender/source/blender/blenkernel/intern/mask_evaluate.c \
	 blender/source/blender/blenkernel/intern/mask_rasterize.c \
	 blender/source/blender/blenkernel/intern/material.c \
	 blender/source/blender/blenkernel/intern/mball.c \
	 blender/source/blender/blenkernel/intern/mesh.c \
	 blender/source/blender/blenkernel/intern/mesh_evaluate.c \
	 blender/source/blender/blenkernel/intern/mesh_mapping.c \
	 blender/source/blender/blenkernel/intern/mesh_validate.c \
	 blender/source/blender/blenkernel/intern/modifier.c \
	 blender/source/blender/blenkernel/intern/modifiers_bmesh.c \
	 blender/source/blender/blenkernel/intern/movieclip.c \
	 blender/source/blender/blenkernel/intern/multires.c \
	 blender/source/blender/blenkernel/intern/nla.c \
	 blender/source/blender/blenkernel/intern/node.c \
	 blender/source/blender/blenkernel/intern/object.c \
	 blender/source/blender/blenkernel/intern/object_deform.c \
	 blender/source/blender/blenkernel/intern/object_dupli.c \
	 blender/source/blender/blenkernel/intern/ocean.c \
	 blender/source/blender/blenkernel/intern/packedFile.c \
	 blender/source/blender/blenkernel/intern/paint.c \
	 blender/source/blender/blenkernel/intern/particle.c \
	 blender/source/blender/blenkernel/intern/particle_system.c \
	 blender/source/blender/blenkernel/intern/pbvh.c \
	 blender/source/blender/blenkernel/intern/pbvh_bmesh.c \
	 blender/source/blender/blenkernel/intern/pointcache.c \
	 blender/source/blender/blenkernel/intern/property.c \
	 blender/source/blender/blenkernel/intern/report.c \
	 blender/source/blender/blenkernel/intern/rigidbody.c \
	 blender/source/blender/blenkernel/intern/sca.c \
	 blender/source/blender/blenkernel/intern/scene.c \
	 blender/source/blender/blenkernel/intern/screen.c \
	 blender/source/blender/blenkernel/intern/seqcache.c \
	 blender/source/blender/blenkernel/intern/seqeffects.c \
	 blender/source/blender/blenkernel/intern/seqmodifier.c \
	 blender/source/blender/blenkernel/intern/sequencer.c \
	 blender/source/blender/blenkernel/intern/shrinkwrap.c \
	 blender/source/blender/blenkernel/intern/sketch.c \
	 blender/source/blender/blenkernel/intern/smoke.c \
	 blender/source/blender/blenkernel/intern/softbody.c \
	 blender/source/blender/blenkernel/intern/sound.c \
	 blender/source/blender/blenkernel/intern/speaker.c \
	 blender/source/blender/blenkernel/intern/subsurf_ccg.c \
	 blender/source/blender/blenkernel/intern/suggestions.c \
	 blender/source/blender/blenkernel/intern/text.c \
	 blender/source/blender/blenkernel/intern/texture.c \
	 blender/source/blender/blenkernel/intern/tracking.c \
	 blender/source/blender/blenkernel/intern/tracking_detect.c \
	 blender/source/blender/blenkernel/intern/tracking_plane_tracker.c \
	 blender/source/blender/blenkernel/intern/tracking_region_tracker.c \
	 blender/source/blender/blenkernel/intern/tracking_solver.c \
	 blender/source/blender/blenkernel/intern/tracking_stabilize.c \
	 blender/source/blender/blenkernel/intern/tracking_util.c \
	 blender/source/blender/blenkernel/intern/treehash.c \
	 blender/source/blender/blenkernel/intern/unit.c \
	 blender/source/blender/blenkernel/intern/world.c \
	 blender/source/blender/blenkernel/intern/writeavi.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_alphaOver.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_bilateralblur.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_blur.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_brightness.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_channelMatte.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_chromaMatte.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_colorMatte.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_colorSpill.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_colorbalance.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_common.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_composite.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_cornerpin.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_crop.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_curves.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_despeckle.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_doubleEdgeMask.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_defocus.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_diffMatte.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_dilate.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_directionalblur.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_displace.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_distanceMatte.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_filter.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_flip.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_gamma.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_glare.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_hueSatVal.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_huecorrect.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_idMask.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_image.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_inpaint.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_invert.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_keyingscreen.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_keying.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_lensdist.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_levels.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_lummaMatte.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_mapUV.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_mapValue.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_mapRange.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_math.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_mask.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_mixrgb.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_movieclip.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_moviedistortion.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_normal.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_normalize.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_outputFile.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_planetrackdeform.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_premulkey.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_rgb.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_rotate.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_scale.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_sepcombHSVA.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_sepcombRGBA.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_sepcombYCCA.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_sepcombYUVA.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_setalpha.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_splitViewer.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_stabilize2d.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_sunbeams.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_texture.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_tonemap.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_trackpos.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_transform.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_translate.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_valToRgb.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_value.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_vecBlur.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_viewer.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_zcombine.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_bokehblur.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_bokehimage.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_boxmask.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_ellipsemask.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_switch.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_colorcorrection.c \
	 blender/source/blender/nodes/composite/nodes/node_composite_pixelate.c \
	 blender/source/blender/nodes/composite/node_composite_tree.c \
	 blender/source/blender/nodes/composite/node_composite_util.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_camera.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_common.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_curves.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_gamma.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_brightness.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_geom.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_hueSatVal.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_invert.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_lamp.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_mapping.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_material.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_math.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_mixRgb.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_normal.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_output.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_rgb.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_sepcombRGB.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_sepcombHSV.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_sepcombXYZ.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_squeeze.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_texture.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_valToRgb.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_value.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_wireframe.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_wavelength.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_blackbody.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_vectMath.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_vectTransform.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_add_shader.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_ambient_occlusion.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_attribute.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_background.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_anisotropic.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_diffuse.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_glass.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_glossy.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_toon.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_refraction.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_translucent.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_transparent.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_velvet.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bsdf_hair.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_bump.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_emission.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_fresnel.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_geometry.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_holdout.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_layer_weight.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_light_falloff.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_light_path.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_mix_shader.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_normal_map.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_object_info.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_hair_info.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_output_lamp.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_output_material.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_output_world.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_output_linestyle.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_particle_info.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_script.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_subsurface_scattering.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tangent.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_brick.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_checker.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_coord.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_environment.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_gradient.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_image.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_magic.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_musgrave.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_noise.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_sky.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_voronoi.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_tex_wave.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_volume_scatter.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_volume_absorption.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_uvAlongStroke.c \
	 blender/source/blender/nodes/shader/nodes/node_shader_uvmap.c \
	 blender/source/blender/nodes/shader/node_shader_tree.c \
	 blender/source/blender/nodes/shader/node_shader_util.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_at.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_bricks.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_checker.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_common.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_compose.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_coord.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_curves.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_decompose.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_distance.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_hueSatVal.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_image.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_invert.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_math.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_mixRgb.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_output.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_proc.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_rotate.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_scale.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_texture.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_translate.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_valToNor.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_valToRgb.c \
	 blender/source/blender/nodes/texture/nodes/node_texture_viewer.c \
	 blender/source/blender/nodes/texture/node_texture_tree.c \
	 blender/source/blender/nodes/texture/node_texture_util.c \
	 blender/source/blender/nodes/intern/node_util.c \
	 blender/source/blender/nodes/intern/node_exec.c \
	 blender/source/blender/nodes/intern/node_common.c \
	 blender/source/blender/nodes/intern/node_socket.c \
	 blender/source/blender/makesrna/intern/rna_access.c \
	 blender_bin/source/blender/makesrna/intern/rna_ID_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_action_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_actuator_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_animation_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_animviz_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_armature_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_boid_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_brush_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_camera_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_cloth_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_color_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_constraint_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_context_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_controller_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_curve_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_dynamicpaint_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_fcurve_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_fluidsim_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_gpencil_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_group_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_image_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_key_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_lamp_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_lattice_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_linestyle_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_main_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_mask_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_material_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_mesh_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_meta_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_modifier_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_movieclip_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_nla_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_nodetree_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_object_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_object_force_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_packedfile_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_particle_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_pose_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_property_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_render_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_rigidbody_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_rna_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_scene_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_screen_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_sculpt_paint_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_sensor_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_sequencer_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_smoke_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_sound_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_space_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_speaker_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_test_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_text_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_texture_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_timeline_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_tracking_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_ui_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_userdef_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_vfont_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_wm_gen.c \
	 blender_bin/source/blender/makesrna/intern/rna_world_gen.c \
	 blender/source/blender/gpu/intern/gpu_buffers.c \
	 blender/source/blender/gpu/intern/gpu_codegen.c \
	 blender/source/blender/gpu/intern/gpu_draw.c \
	 blender/source/blender/gpu/intern/gpu_extensions.c \
	 blender/source/blender/gpu/intern/gpu_init_exit.c \
	 blender/source/blender/gpu/intern/gpu_material.c \
	 blender/source/blender/gpu/intern/gpu_simple_shader.c \
	 blender/source/blender/gpu/intern/gpu_select.c \
	 blender_bin/source/blender/gpu/shaders/gpu_shader_material.glsl.c \
	 blender_bin/source/blender/gpu/shaders/gpu_shader_sep_gaussian_blur_frag.glsl.c \
	 blender_bin/source/blender/gpu/shaders/gpu_shader_sep_gaussian_blur_vert.glsl.c \
	 blender_bin/source/blender/gpu/shaders/gpu_shader_simple_frag.glsl.c \
	 blender_bin/source/blender/gpu/shaders/gpu_shader_simple_vert.glsl.c \
	 blender_bin/source/blender/gpu/shaders/gpu_shader_vertex.glsl.c \
	 blender_bin/source/blender/gpu/shaders/gpu_shader_vsm_store_frag.glsl.c \
	 blender_bin/source/blender/gpu/shaders/gpu_shader_vsm_store_vert.glsl.c \
	 blender/source/blender/blenloader/intern/readblenentry.c \
	 blender/source/blender/blenloader/intern/readfile.c \
	 blender/source/blender/blenloader/intern/runtime.c \
	 blender/source/blender/blenloader/intern/undofile.c \
	 blender/source/blender/blenloader/intern/versioning_250.c \
	 blender/source/blender/blenloader/intern/versioning_260.c \
	 blender/source/blender/blenloader/intern/versioning_270.c \
	 blender/source/blender/blenloader/intern/versioning_defaults.c \
	 blender/source/blender/blenloader/intern/versioning_legacy.c \
	 blender/source/blender/blenloader/intern/writefile.c \
	 blender/source/blender/imbuf/intern/allocimbuf.c \
	 blender/source/blender/imbuf/intern/anim_movie.c \
	 blender/source/blender/imbuf/intern/bmp.c \
	 blender/source/blender/imbuf/intern/cache.c \
	 blender/source/blender/imbuf/intern/colormanagement.c \
	 blender/source/blender/imbuf/intern/divers.c \
	 blender/source/blender/imbuf/intern/filetype.c \
	 blender/source/blender/imbuf/intern/filter.c \
	 blender/source/blender/imbuf/intern/imageprocess.c \
	 blender/source/blender/imbuf/intern/indexer.c \
	 blender/source/blender/imbuf/intern/indexer_dv.c \
	 blender/source/blender/imbuf/intern/iris.c \
	 blender/source/blender/imbuf/intern/jpeg.c \
	 blender/source/blender/imbuf/intern/metadata.c \
	 blender/source/blender/imbuf/intern/module.c \
	 blender/source/blender/imbuf/intern/moviecache.c \
	 blender/source/blender/imbuf/intern/png.c \
	 blender/source/blender/imbuf/intern/readimage.c \
	 blender/source/blender/imbuf/intern/rectop.c \
	 blender/source/blender/imbuf/intern/rotate.c \
	 blender/source/blender/imbuf/intern/scaling.c \
	 blender/source/blender/imbuf/intern/targa.c \
	 blender/source/blender/imbuf/intern/thumbs.c \
	 blender/source/blender/imbuf/intern/thumbs_blend.c \
	 blender/source/blender/imbuf/intern/util.c \
	 blender/source/blender/imbuf/intern/writeimage.c \
	 blender/source/blender/imbuf/intern/openexr/openexr_stub.cpp \
	 blender/source/blender/blenlib/intern/BLI_args.c \
	 blender/source/blender/blenlib/intern/BLI_array.c \
	 blender/source/blender/blenlib/intern/BLI_dial.c \
	 blender/source/blender/blenlib/intern/BLI_dynstr.c \
	 blender/source/blender/blenlib/intern/BLI_ghash.c \
	 blender/source/blender/blenlib/intern/BLI_heap.c \
	 blender/source/blender/blenlib/intern/BLI_kdopbvh.c \
	 blender/source/blender/blenlib/intern/BLI_kdtree.c \
	 blender/source/blender/blenlib/intern/BLI_linklist.c \
	 blender/source/blender/blenlib/intern/BLI_memarena.c \
	 blender/source/blender/blenlib/intern/BLI_mempool.c \
	 blender/source/blender/blenlib/intern/DLRB_tree.c \
	 blender/source/blender/blenlib/intern/boxpack2d.c \
	 blender/source/blender/blenlib/intern/buffer.c \
	 blender/source/blender/blenlib/intern/callbacks.c \
	 blender/source/blender/blenlib/intern/convexhull2d.c \
	 blender/source/blender/blenlib/intern/easing.c \
	 blender/source/blender/blenlib/intern/edgehash.c \
	 blender/source/blender/blenlib/intern/endian_switch.c \
	 blender/source/blender/blenlib/intern/fileops.c \
	 blender/source/blender/blenlib/intern/freetypefont.c \
	 blender/source/blender/blenlib/intern/graph.c \
	 blender/source/blender/blenlib/intern/gsqueue.c \
	 blender/source/blender/blenlib/intern/jitter.c \
	 blender/source/blender/blenlib/intern/lasso.c \
	 blender/source/blender/blenlib/intern/listbase.c \
	 blender/source/blender/blenlib/intern/math_base.c \
	 blender/source/blender/blenlib/intern/math_base_inline.c \
	 blender/source/blender/blenlib/intern/math_color.c \
	 blender/source/blender/blenlib/intern/math_color_blend_inline.c \
	 blender/source/blender/blenlib/intern/math_color_inline.c \
	 blender/source/blender/blenlib/intern/math_geom.c \
	 blender/source/blender/blenlib/intern/math_geom_inline.c \
	 blender/source/blender/blenlib/intern/math_interp.c \
	 blender/source/blender/blenlib/intern/math_matrix.c \
	 blender/source/blender/blenlib/intern/math_rotation.c \
	 blender/source/blender/blenlib/intern/math_vector.c \
	 blender/source/blender/blenlib/intern/math_vector_inline.c \
	 blender/source/blender/blenlib/intern/md5.c \
	 blender/source/blender/blenlib/intern/noise.c \
	 blender/source/blender/blenlib/intern/path_util.c \
	 blender/source/blender/blenlib/intern/polyfill2d.c \
	 blender/source/blender/blenlib/intern/quadric.c \
	 blender/source/blender/blenlib/intern/rand.c \
	 blender/source/blender/blenlib/intern/rct.c \
	 blender/source/blender/blenlib/intern/scanfill.c \
	 blender/source/blender/blenlib/intern/scanfill_utils.c \
	 blender/source/blender/blenlib/intern/smallhash.c \
	 blender/source/blender/blenlib/intern/sort.c \
	 blender/source/blender/blenlib/intern/sort_utils.c \
	 blender/source/blender/blenlib/intern/stack.c \
	 blender/source/blender/blenlib/intern/storage.c \
	 blender/source/blender/blenlib/intern/string.c \
	 blender/source/blender/blenlib/intern/string_cursor_utf8.c \
	 blender/source/blender/blenlib/intern/string_utf8.c \
	 blender/source/blender/blenlib/intern/system.c \
	 blender/source/blender/blenlib/intern/task.c \
	 blender/source/blender/blenlib/intern/threads.c \
	 blender/source/blender/blenlib/intern/time.c \
	 blender/source/blender/blenlib/intern/timecode.c \
	 blender/source/blender/blenlib/intern/uvproject.c \
	 blender/source/blender/blenlib/intern/voronoi.c \
	 blender/source/blender/blenlib/intern/voxel.c \
	 blender/intern/ghost/intern/GHOST_Buttons.cpp \
	 blender/intern/ghost/intern/GHOST_C-api.cpp \
	 blender/intern/ghost/intern/GHOST_CallbackEventConsumer.cpp \
	 blender/intern/ghost/intern/GHOST_Context.cpp \
	 blender/intern/ghost/intern/GHOST_ContextNone.cpp \
	 blender/intern/ghost/intern/GHOST_DisplayManager.cpp \
	 blender/intern/ghost/intern/GHOST_EventManager.cpp \
	 blender/intern/ghost/intern/GHOST_ISystem.cpp \
	 blender/intern/ghost/intern/GHOST_ISystemPaths.cpp \
	 blender/intern/ghost/intern/GHOST_ModifierKeys.cpp \
	 blender/intern/ghost/intern/GHOST_Path-api.cpp \
	 blender/intern/ghost/intern/GHOST_Rect.cpp \
	 blender/intern/ghost/intern/GHOST_System.cpp \
	 blender/intern/ghost/intern/GHOST_TimerManager.cpp \
	 blender/intern/ghost/intern/GHOST_Window.cpp \
	 blender/intern/ghost/intern/GHOST_WindowManager.cpp \
	 blender/intern/ghost/intern/SPEC_SystemPathsSelect.cpp \
	 blender/intern/string/intern/STR_String.cpp \
	 blender/intern/memutil/intern/MEM_CacheLimiterC-Api.cpp \
	 blender/intern/memutil/intern/MEM_RefCountedC-Api.cpp \
	 blender/intern/guardedalloc/intern/mallocn.c \
	 blender/intern/guardedalloc/intern/mallocn_guarded_impl.c \
	 blender/intern/guardedalloc/intern/mallocn_lockfree_impl.c \
	 blender/extern/colamd/Source/colamd.c \
	 blender/extern/colamd/Source/colamd_global.c \
	 blender/source/blender/makesdna/intern/dna_genfile.c \
	 blender_bin/source/blender/makesdna/intern/dna.c \
	 blender/source/blender/blenfont/intern/blf.c \
	 blender/source/blender/blenfont/intern/blf_dir.c \
	 blender/source/blender/blenfont/intern/blf_font.c \
	 blender/source/blender/blenfont/intern/blf_glyph.c \
	 blender/source/blender/blenfont/intern/blf_lang.c \
	 blender/source/blender/blenfont/intern/blf_translation.c \
	 blender/source/blender/blenfont/intern/blf_util.c \
	 blender/intern/mikktspace/mikktspace.c blender/intern/raskter/raskter.c \
	 blender/intern/opencolorio/ocio_capi.cc \
	 blender/intern/opencolorio/fallback_impl.cc \
	 blender/extern/rangetree/range_tree_c_api.cc \
	 blender/extern/wcwidth/wcwidth.c blender/extern/libmv/intern/stub.cc \
	 blender/intern/glew-mx/intern/glew-mx.c blender/extern/glew/src/glew.c \
	 spec_gl.c spec_glcorearb.c spec_glu.c spec_glx.c spec_jpeg.c spec_ft.c \
	 zlib/adler32.c zlib/compress.c zlib/crc32.c zlib/deflate.c \
	 zlib/gzclose.c zlib/gzlib.c zlib/gzread.c zlib/gzwrite.c zlib/infback.c \
	 zlib/inflate.c zlib/inftrees.c zlib/trees.c zlib/uncompr.c zlib/zutil.c \
	 zlib/inffast.c libpng/png.c libpng/pngset.c libpng/pngget.c \
	 libpng/pngrutil.c libpng/pngtrans.c libpng/pngwutil.c libpng/pngmem.c \
	 libpng/pngpread.c libpng/pngread.c libpng/pngerror.c libpng/pngwrite.c \
	 libpng/pngrtran.c libpng/pngwtran.c libpng/pngrio.c libpng/pngwio.c \
	 specrand/specrand.c spec_backtrace.c
EXEBASE=blender_r
NEED_MATH=yes
BENCHLANG=CXX C

BENCH_FLAGS      = -Ispecrand -Iblender/extern/binreloc/include -Iblender/extern/colamd/Include -Iblender/extern/glew/include -Iblender/extern/libmv -Iblender/extern/libmv/intern -Iblender/extern/rangetree -Iblender/extern/wcwidth -Iblender/intern -Iblender/intern/atomic -Iblender/intern/audaspace/intern -Iblender/intern/cycles/blender -Iblender/intern/elbeem/extern -Iblender/intern/ghost -Iblender/intern/ghost/intern -Iblender/intern/glew-mx -Iblender/intern/glew-mx/intern -Iblender/intern/guardedalloc -Iblender/intern/guardedalloc/intern -Iblender/intern/iksolver/extern -Iblender/intern/locale -Iblender/intern/memutil -Iblender/intern/mikktspace -Iblender/intern/opencolorio -Iblender/intern/raskter -Iblender/intern/smoke/extern -Iblender/intern/string -Iblender/intern/utfconv -Iblender/source/blender/blenfont -Iblender/source/blender/blenfont/intern -Iblender/source/blender/blenkernel -Iblender/source/blender/blenkernel/intern -Iblender/source/blender/blenlib -Iblender/source/blender/blenlib/intern -Iblender/source/blender/blenloader -Iblender/source/blender/blenloader/intern -Iblender/source/blender/bmesh -Iblender/source/blender/bmesh/intern -Iblender/source/blender/bmesh/tools -Iblender/source/blender/collada -Iblender/source/blender/compositor -Iblender/source/blender/editors/animation -Iblender/source/blender/editors/armature -Iblender/source/blender/editors/curve -Iblender/source/blender/editors/gpencil -Iblender/source/blender/editors/include -Iblender/source/blender/editors/interface -Iblender/source/blender/editors/io -Iblender/source/blender/editors/mask -Iblender/source/blender/editors/mesh -Iblender/source/blender/editors/metaball -Iblender/source/blender/editors/object -Iblender/source/blender/editors/physics -Iblender/source/blender/editors/render -Iblender/source/blender/editors/screen -Iblender/source/blender/editors/sculpt_paint -Iblender/source/blender/editors/sound -Iblender/source/blender/editors/space_action -Iblender/source/blender/editors/space_buttons -Iblender/source/blender/editors/space_clip -Iblender/source/blender/editors/space_console -Iblender/source/blender/editors/space_file -Iblender/source/blender/editors/space_graph -Iblender/source/blender/editors/space_image -Iblender/source/blender/editors/space_info -Iblender/source/blender/editors/space_logic -Iblender/source/blender/editors/space_nla -Iblender/source/blender/editors/space_node -Iblender/source/blender/editors/space_outliner -Iblender/source/blender/editors/space_script -Iblender/source/blender/editors/space_sequencer -Iblender/source/blender/editors/space_text -Iblender/source/blender/editors/space_time -Iblender/source/blender/editors/space_userpref -Iblender/source/blender/editors/space_view3d -Iblender/source/blender/editors/transform -Iblender/source/blender/editors/util -Iblender/source/blender/editors/uvedit -Iblender/source/blender/gpu -Iblender/source/blender/gpu/intern -Iblender/source/blender/ikplugin -Iblender/source/blender/ikplugin/intern -Iblender/source/blender/imbuf -Iblender/source/blender/imbuf/intern -Iblender/source/blender/imbuf/intern/openexr -Iblender/source/blender/makesdna -Iblender/source/blender/makesrna -Iblender/source/blender/makesrna/intern -Iblender/source/blender/modifiers -Iblender/source/blender/modifiers/intern -Iblender/source/blender/nodes -Iblender/source/blender/nodes/composite -Iblender/source/blender/nodes/intern -Iblender/source/blender/nodes/shader -Iblender/source/blender/nodes/texture -Iblender/source/blender/python -Iblender/source/blender/render/extern/include -Iblender/source/blender/render/intern/include -Iblender/source/blender/render/intern/raytrace -Iblender/source/blender/windowmanager -Iblender/source/gameengine/BlenderRoutines -Iblender_bin/source/blender/makesrna/intern -Iinclude -Ilibpng -Izlib -DSPEC_AUTO_SUPPRESS_OPENMP -DSPEC_AUTO_BYTEORDER=0x12345678 -DGLEW_NO_ES -DGLEW_STATIC -DWITH_DNA_GHASH -DWITH_GL_PROFILE_COMPAT -DWITH_HEADLESS -DHAVE_UNSIGNED_CHAR
CC               = $(SPECLANG)gcc     -std=c99   -m64
CC_VERSION_OPTION = -v
CXX              = $(SPECLANG)g++     -std=c++03 -m64
CXX_VERSION_OPTION = -v
EXTRA_PORTABILITY = -DSPEC_LP64
FC               = $(SPECLANG)gfortran           -m64
FC_VERSION_OPTION = -v
OPTIMIZE         = -g -O3 -march=native -fno-unsafe-math-optimizations  -fno-tree-loop-vectorize
OS               = unix
PORTABILITY      = -funsigned-char -DSPEC_LINUX
SPECLANG         = /usr/bin/
absolutely_no_locking = 0
abstol           = 
action           = buildsetup
allow_label_override = 0
backup_config    = 1
baseexe          = blender_r
basepeak         = 1
benchdir         = benchspec
benchmark        = 526.blender_r
binary           = 
bindir           = exe
builddir         = build
bundleaction     = 
bundlename       = 
calctol          = 1
changedhash      = 0
check_version    = 0
clean_between_builds = no
command_add_redirect = 1
commanderrfile   = speccmds.err
commandexe       = blender_r_base.primeiro-teste-m64
commandfile      = speccmds.cmd
commandoutfile   = speccmds.out
commandstdoutfile = speccmds.stdout
comparedir       = compare
compareerrfile   = compare.err
comparefile      = compare.cmd
compareoutfile   = compare.out
comparestdoutfile = compare.stdout
compile_error    = 0
compwhite        = 
configdir        = config
configfile       = default.cfg
configpath       = /home/kratos/specs/2017/config/default.cfg
copies           = 1
current_range    = 
datadir          = data
default_size     = ref
default_submit   = $command
delay            = 0
deletebinaries   = 0
deletework       = 0
dependent_workloads = 0
device           = 
difflines        = 10
dirprot          = 511
discard_power_samples = 0
enable_monitor   = 1
endian           = 12345678
env_vars         = 0
expand_notes     = 0
expid            = 
exthash_bits     = 256
failflags        = 0
fake             = 0
feedback         = 1
flag_url_base    = https://www.spec.org/auto/cpu2017/Docs/benchmarks/flags/
floatcompare     = 
force_monitor    = 0
from_runcpu      = 2
fw_bios          = virtualbox
hostname         = six-seven
http_proxy       = 
http_timeout     = 30
hw_avail         = Ago-2025
hw_cpu_max_mhz   = 4100
hw_cpu_name      = AMD Ryzen 7 5700X3D
hw_cpu_nominal_mhz = 3000
hw_disk          = 1 TB SSD NVMe
hw_memory001     = 16 GB (1 x 16 GB DDR4-3200)
hw_memory002     = 'N GB (N x N GB nRxn PC4-nnnnX-X)'
hw_model         = 'Test Build'
hw_nchips        = 1
hw_ncores        = 5
hw_ncpuorder     = 1-5 chips
hw_nthreadspercore = 2
hw_ocache        = None
hw_other         = None
hw_pcache        = 64 KB I + 64 KB D on chip per core
hw_scache        = 512 KB I+D on chip per core
hw_tcache        = 96 MB I+D on chip
hw_vendor        = My Test
idle_current_range = 
idledelay        = 10
idleduration     = 60
ignore_errors    = 1
ignore_sigint    = 0
ignorecase       = 
info_wrap_columns = 50
inputdir         = input
inputgenerrfile  = inputgen.err
inputgenfile     = inputgen.cmd
inputgenoutfile  = inputgen.out
inputgenstdoutfile = inputgen.stdout
iteration        = -1
iterations       = 1
keeptmp          = 0
label            = primeiro-teste-m64
license_num      = 2017
line_width       = 1020
link_input_files = 1
locking          = 1
log              = CPU2017
log_line_width   = 1020
log_timestamp    = 0
logfile          = /home/kratos/specs/2017/tmp/CPU2017.002/templogs/preenv.fprate.002.0
logname          = /home/kratos/specs/2017/tmp/CPU2017.002/templogs/preenv.fprate.002.0
lognum           = 002.0
mail_reports     = all
mailcompress     = 0
mailmethod       = smtp
mailport         = 25
mailserver       = 127.0.0.1
mailto           = 
make             = specmake
make_no_clobber  = 0
makefile_template = Makefile.YYYtArGeTYYYspec
makeflags        = --jobs=8
max_average_uncertainty = 1
max_hum_limit    = 0
max_report_runs  = 3
max_unknown_uncertainty = 1
mean_anyway      = 1
meter_connect_timeout = 30
meter_errors_default = 5
meter_errors_percentage = 5
min_report_runs  = 2
min_temp_limit   = 20
minimize_builddirs = 0
minimize_rundirs = 0
name             = blender_r
nansupport       = 
need_math        = yes
no_input_handler = close
no_monitor       = 
noratios         = 0
note_preenv      = 1
notes_plat_sysinfo_000 = 
notes_plat_sysinfo_005 =  Sysinfo program /home/kratos/specs/2017/bin/sysinfo
notes_plat_sysinfo_010 =  Rev: r6365 of 2019-08-21 295195f888a3d7edb1e6e46a485a0011
notes_plat_sysinfo_015 =  running on six-seven Sat Oct 11 18:48:45 2025
notes_plat_sysinfo_020 = 
notes_plat_sysinfo_025 =  SUT (System Under Test) info as seen by some common utilities.
notes_plat_sysinfo_030 =  For more information on this section, see
notes_plat_sysinfo_035 =     https://www.spec.org/cpu2017/Docs/config.html\#sysinfo
notes_plat_sysinfo_040 = 
notes_plat_sysinfo_045 =  From /proc/cpuinfo
notes_plat_sysinfo_050 =     model name : AMD Ryzen 7 5700X3D 8-Core Processor
notes_plat_sysinfo_055 =        1  "physical id"s (chips)
notes_plat_sysinfo_060 =        5 "processors"
notes_plat_sysinfo_065 =     cores, siblings (Caution: counting these is hw and system dependent. The following
notes_plat_sysinfo_070 =     excerpts from /proc/cpuinfo might not be reliable.  Use with caution.)
notes_plat_sysinfo_075 =        cpu cores : 5
notes_plat_sysinfo_080 =        siblings  : 5
notes_plat_sysinfo_085 =        physical 0: cores 0 1 2 3 4
notes_plat_sysinfo_090 = 
notes_plat_sysinfo_095 =  From lscpu:
notes_plat_sysinfo_100 =       Architecture:                            x86_64
notes_plat_sysinfo_105 =       CPU op-mode(s):                          32-bit, 64-bit
notes_plat_sysinfo_110 =       Address sizes:                           48 bits physical, 48 bits virtual
notes_plat_sysinfo_115 =       Byte Order:                              Little Endian
notes_plat_sysinfo_120 =       CPU(s):                                  5
notes_plat_sysinfo_125 =       On-line CPU(s) list:                     0-4
notes_plat_sysinfo_130 =       Vendor ID:                               AuthenticAMD
notes_plat_sysinfo_135 =       Model name:                              AMD Ryzen 7 5700X3D 8-Core Processor
notes_plat_sysinfo_140 =       CPU family:                              25
notes_plat_sysinfo_145 =       Model:                                   33
notes_plat_sysinfo_150 =       Thread(s) per core:                      1
notes_plat_sysinfo_155 =       Core(s) per socket:                      5
notes_plat_sysinfo_160 =       Socket(s):                               1
notes_plat_sysinfo_165 =       Stepping:                                2
notes_plat_sysinfo_170 =       BogoMIPS:                                5999.99
notes_plat_sysinfo_175 =       Flags:                                   fpu vme de pse tsc msr pae mce cx8 apic sep
notes_plat_sysinfo_180 =       mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt
notes_plat_sysinfo_185 =       rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid tsc_known_freq
notes_plat_sysinfo_190 =       pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c
notes_plat_sysinfo_195 =       rdrand hypervisor lahf_lm cmp_legacy cr8_legacy abm sse4a misalignsse 3dnowprefetch
notes_plat_sysinfo_200 =       vmmcall fsgsbase bmi1 avx2 bmi2 invpcid rdseed adx clflushopt sha_ni arat debug_swap
notes_plat_sysinfo_205 =       Hypervisor vendor:                       KVM
notes_plat_sysinfo_210 =       Virtualization type:                     full
notes_plat_sysinfo_215 =       L1d cache:                               160 KiB (5 instances)
notes_plat_sysinfo_220 =       L1i cache:                               160 KiB (5 instances)
notes_plat_sysinfo_225 =       L2 cache:                                2.5 MiB (5 instances)
notes_plat_sysinfo_230 =       L3 cache:                                480 MiB (5 instances)
notes_plat_sysinfo_235 =       NUMA node(s):                            1
notes_plat_sysinfo_240 =       NUMA node0 CPU(s):                       0-4
notes_plat_sysinfo_245 =       Vulnerability Gather data sampling:      Not affected
notes_plat_sysinfo_250 =       Vulnerability Ghostwrite:                Not affected
notes_plat_sysinfo_255 =       Vulnerability Indirect target selection: Not affected
notes_plat_sysinfo_260 =       Vulnerability Itlb multihit:             Not affected
notes_plat_sysinfo_265 =       Vulnerability L1tf:                      Not affected
notes_plat_sysinfo_270 =       Vulnerability Mds:                       Not affected
notes_plat_sysinfo_275 =       Vulnerability Meltdown:                  Not affected
notes_plat_sysinfo_280 =       Vulnerability Mmio stale data:           Not affected
notes_plat_sysinfo_285 =       Vulnerability Reg file data sampling:    Not affected
notes_plat_sysinfo_290 =       Vulnerability Retbleed:                  Not affected
notes_plat_sysinfo_295 =       Vulnerability Spec rstack overflow:      Vulnerable: Safe RET, no microcode
notes_plat_sysinfo_300 =       Vulnerability Spec store bypass:         Not affected
notes_plat_sysinfo_305 =       Vulnerability Spectre v1:                Mitigation; usercopy/swapgs barriers and
notes_plat_sysinfo_310 =       __user pointer sanitization
notes_plat_sysinfo_315 =       Vulnerability Spectre v2:                Mitigation; Retpolines; STIBP disabled; RSB
notes_plat_sysinfo_320 =       filling; PBRSB-eIBRS Not affected; BHI Not affected
notes_plat_sysinfo_325 =       Vulnerability Srbds:                     Not affected
notes_plat_sysinfo_330 =       Vulnerability Tsx async abort:           Not affected
notes_plat_sysinfo_335 = 
notes_plat_sysinfo_340 =  /proc/cpuinfo cache data
notes_plat_sysinfo_345 =     cache size : 512 KB
notes_plat_sysinfo_350 = 
notes_plat_sysinfo_355 =  From numactl --hardware  WARNING: a numactl 'node' might or might not correspond to a
notes_plat_sysinfo_360 =  physical chip.
notes_plat_sysinfo_365 =    available: 1 nodes (0)
notes_plat_sysinfo_370 =    node 0 cpus: 0 1 2 3 4
notes_plat_sysinfo_375 =    node 0 size: 8593 MB
notes_plat_sysinfo_380 =    node 0 free: 1365 MB
notes_plat_sysinfo_385 =    node distances:
notes_plat_sysinfo_390 =    node   0
notes_plat_sysinfo_395 =      0:  10
notes_plat_sysinfo_400 = 
notes_plat_sysinfo_405 =  From /proc/meminfo
notes_plat_sysinfo_410 =     MemTotal:        8799764 kB
notes_plat_sysinfo_415 =     HugePages_Total:       0
notes_plat_sysinfo_420 =     Hugepagesize:       2048 kB
notes_plat_sysinfo_425 = 
notes_plat_sysinfo_430 =  /usr/bin/lsb_release -d
notes_plat_sysinfo_435 =     Ubuntu 24.04.3 LTS
notes_plat_sysinfo_440 = 
notes_plat_sysinfo_445 =  From /etc/*release* /etc/*version*
notes_plat_sysinfo_450 =     debian_version: trixie/sid
notes_plat_sysinfo_455 =     os-release:
notes_plat_sysinfo_460 =        PRETTY_NAME="Ubuntu 24.04.3 LTS"
notes_plat_sysinfo_465 =        NAME="Ubuntu"
notes_plat_sysinfo_470 =        VERSION_ID="24.04"
notes_plat_sysinfo_475 =        VERSION="24.04.3 LTS (Noble Numbat)"
notes_plat_sysinfo_480 =        VERSION_CODENAME=noble
notes_plat_sysinfo_485 =        ID=ubuntu
notes_plat_sysinfo_490 =        ID_LIKE=debian
notes_plat_sysinfo_495 =        HOME_URL="https://www.ubuntu.com/"
notes_plat_sysinfo_500 = 
notes_plat_sysinfo_505 =  uname -a:
notes_plat_sysinfo_510 =     Linux six-seven 6.14.0-33-generic \#33~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep 19
notes_plat_sysinfo_515 =     17:02:30 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
notes_plat_sysinfo_520 = 
notes_plat_sysinfo_525 =  Kernel self-reported vulnerability status:
notes_plat_sysinfo_530 = 
notes_plat_sysinfo_535 =  gather_data_sampling:                     Not affected
notes_plat_sysinfo_540 =  ghostwrite:                               Not affected
notes_plat_sysinfo_545 =  indirect_target_selection:                Not affected
notes_plat_sysinfo_550 =  itlb_multihit:                            Not affected
notes_plat_sysinfo_555 =  CVE-2018-3620 (L1 Terminal Fault):        Not affected
notes_plat_sysinfo_560 =  Microarchitectural Data Sampling:         Not affected
notes_plat_sysinfo_565 =  CVE-2017-5754 (Meltdown):                 Not affected
notes_plat_sysinfo_570 =  mmio_stale_data:                          Not affected
notes_plat_sysinfo_575 =  reg_file_data_sampling:                   Not affected
notes_plat_sysinfo_580 =  retbleed:                                 Not affected
notes_plat_sysinfo_585 =  spec_rstack_overflow:                     Vulnerable: Safe RET, no microcode
notes_plat_sysinfo_590 =  CVE-2018-3639 (Speculative Store Bypass): Not affected
notes_plat_sysinfo_595 =  CVE-2017-5753 (Spectre variant 1):        Mitigation: usercopy/swapgs barriers and __user
notes_plat_sysinfo_600 =                                            pointer sanitization
notes_plat_sysinfo_605 =  CVE-2017-5715 (Spectre variant 2):        Mitigation: Retpolines; STIBP: disabled; RSB
notes_plat_sysinfo_610 =                                            filling; PBRSB-eIBRS: Not affected; BHI: Not
notes_plat_sysinfo_615 =                                            affected
notes_plat_sysinfo_620 =  srbds:                                    Not affected
notes_plat_sysinfo_625 =  tsx_async_abort:                          Not affected
notes_plat_sysinfo_630 = 
notes_plat_sysinfo_635 =  run-level 5 Oct 10 16:07
notes_plat_sysinfo_640 = 
notes_plat_sysinfo_645 =  SPEC is set to: /home/kratos/specs/2017
notes_plat_sysinfo_650 =     Filesystem     Type  Size  Used Avail Use% Mounted on
notes_plat_sysinfo_655 =     /dev/sda2      ext4   98G   32G   62G  34% /
notes_plat_sysinfo_660 = 
notes_plat_sysinfo_665 =  From /sys/devices/virtual/dmi/id
notes_plat_sysinfo_670 =      BIOS:    innotek GmbH VirtualBox 12/01/2006
notes_plat_sysinfo_675 =      Vendor:  innotek GmbH
notes_plat_sysinfo_680 =      Product: VirtualBox
notes_plat_sysinfo_685 =      Product Family: Virtual Machine
notes_plat_sysinfo_690 = 
notes_plat_sysinfo_695 =  Cannot run dmidecode; consider saying (as root)
notes_plat_sysinfo_700 =     chmod +s /usr/sbin/dmidecode
notes_plat_sysinfo_705 = 
notes_plat_sysinfo_710 =  (End of data from sysinfo program)
notes_wrap_columns = 0
notes_wrap_indent =   
num              = 526
obiwan           = 
os_exe_ext       = 
output_format    = txt,html,cfg,pdf,csv
output_root      = 
outputdir        = output
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /home/kratos/specs/2017/benchspec/CPU/526.blender_r
plain_train      = 1
platform         = 
power            = 0
preENV_LD_LIBRARY_PATH = %{gcc_dir}/lib64/:%{gcc_dir}/lib/:/lib64
preenv           = 0
prefix           = 
prepared_by      = Watta
ranks            = 1
rawhash_bits     = 256
rebuild          = 0
reftime          = reftime
reportable       = 0
resultdir        = result
review           = 0
run              = all
runcpu           = /home/kratos/specs/2017/bin/harness/runcpu --action buildsetup --noreportable --nopower --runmode rate --tune base --size refrate fprate --nopreenv --note-preenv --logfile /home/kratos/specs/2017/tmp/CPU2017.002/templogs/preenv.fprate.002.0 --lognum 002.0 --from_runcpu 2
rundir           = run
runmode          = rate
safe_eval        = 1
save_build_files = 
section_specifier_fatal = 1
setprocgroup     = 1
setup_error      = 0
sigint           = 2
size             = refrate
size_class       = ref
skipabstol       = 
skipobiwan       = 
skipreltol       = 
skiptol          = 
smarttune        = base
specdiff         = specdiff
specrun          = specinvoke
srcalt           = 
srcdir           = src
srcsource        = /home/kratos/specs/2017/benchspec/CPU/526.blender_r/src
stagger          = 10
strict_rundir_verify = 1
sw_avail         = Ago-2025
sw_base_ptrsize  = 64-bit
sw_compiler001   = C/C++/Fortran: Version 11.4.0 of GCC, the
sw_compiler002   = GNU Compiler Collection
sw_file          = ext4
sw_os001         = Ubuntu 22.04.5 LTS
sw_os002         = 6.14.0-33-generic
sw_other         = None
sw_peak_ptrsize  = Not Applicable
sw_state         = 
sysinfo_hash_bits = 256
sysinfo_program  = specperl /home/kratos/specs/2017/bin/sysinfo
sysinfo_program_hash = sysinfo:SHA:1b187da62efa5d65f0e989c214b6a257d16a31d3cf135973c9043da741052207
table            = 1
teeout           = 0
test_date        = Oct-2025
test_sponsor     = My Test
tester           = My Test
threads          = 1
top              = /home/kratos/specs/2017
train_single_thread = 0
train_with       = train
tune             = base
uid              = 1000
unbuffer         = 1
uncertainty_exception = 5
update           = 0
update_url       = http://www.spec.org/auto/cpu2017/updates/
use_submit_for_compare = 0
use_submit_for_speed = 0
username         = kratos
verbose          = 5
verify_binaries  = 1
version          = 1.000503
voltage_range    = 
worklist         = list
OUTPUT_RMFILES   = imagevalidate_sh5_reduced_0234.out
