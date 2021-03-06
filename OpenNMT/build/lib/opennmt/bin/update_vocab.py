"""Script to update vocabularies in a checkpoint."""

import argparse

import tensorflow as tf

from opennmt.utils import checkpoint


def main():
  tf.logging.set_verbosity(tf.logging.INFO)

  parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument("--model_dir", required=True,
                      help="The model directory containing the checkpoints.")
  parser.add_argument("--output_dir", required=True,
                      help="The output directory where the updated checkpoint will be saved.")
  parser.add_argument("--src_vocab", default=None,
                      help="Path to the current source vocabulary.")
  parser.add_argument("--tgt_vocab", default=None,
                      help="Path to the current target vocabulary.")
  parser.add_argument("--shared_vocab", default=None,
                      help="Path to the current shared vocabulary.")
  parser.add_argument("--new_src_vocab", default=None,
                      help="Path to the new source vocabulary.")
  parser.add_argument("--new_tgt_vocab", default=None,
                      help="Path to the new target vocabulary.")
  parser.add_argument("--new_shared_vocab", default=None,
                      help="Path to the new shared vocabulary.")
  #parser.add_argument("--shared_embeddings", default=False, action="store_true",
  #                    help="Update vocabulary of a model trained using a shared embedding.")
  parser.add_argument("--mode", default="merge", choices=["merge", "replace"],
                      help="Vocabulary update mode.")
  args = parser.parse_args()

  checkpoint.update_vocab(args.model_dir,
                          args.output_dir,
                          args.src_vocab,
                          args.tgt_vocab,
                          args.shared_vocab,
                          args.new_src_vocab,
                          args.new_tgt_vocab,
                          args.new_shared_vocab,
                          args.mode,
                          session_config=tf.ConfigProto(device_count={"GPU": 0}))
                          # args.shared_embeddings,


if __name__ == "__main__":
  main()
