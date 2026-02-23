# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-02-23 00:30:36

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 165
- **总 Thread 数**: 20
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 19 threads (158 邮件)
- **Other**: 1 threads (7 邮件)

---

## 📌 PATCH

共 19 个 thread

---

### Thread 1: [PATCH v12 00/30] Tracefs support for pKVM

**📧 邮件数**: 36 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 19 Feb 2026 15:02:37 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（PATCH v12 00/30）。该补丁的主要内容是为 pKVM 超级管理程序引入 Tracefs 支持，以便更好地进行调试和性能分析。

1. **原始补丁/问题的内容**：补丁系列的目标是为 pKVM 提供一个简单易用的 Tracefs 接口，支持远程事件和缓冲区的创建。补丁中引入了新的环形缓冲区实现，允许超管程序写入事件，内核则作为读取者。

2. **之前讨论的要点**：在历史讨论中，参与者强调了 Tracefs 在调试和性能分析中的重要性，并讨论了如何实现远程事件的创建和管理。补丁的设计考虑了与现有工具的兼容性，并确保了内核和超管程序之间的有效数据共享。

3. **本周的新讨论、进展或结论**：本周的讨论主要集中在补丁的具体实现和测试上。Vincent Donnefort 提交了多个补丁，增加了对环形缓冲区的支持、事件的创建以及 Tracefs 接口的实现。Steven Rostedt 对补丁进行了审核，并提出了在合并过程中可能出现的冲突，建议在下一个合并窗口前先将 Tracefs 部分合并到一个分支中，以减少冲突。Marc Zyngier 也对此表示支持，并希望在合并后获取相关链接。

整体来看，本次讨论为 pKVM 的 Tracefs 支持奠定了基础，确保了未来的调试和性能分析工作能够顺利进行。

#### 📝 邮件列表

1. **[02-19 15:02]** [PATCH v12 00/30] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[02-19 15:02]** [PATCH v12 01/30] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[02-19 15:02]** [PATCH v12 02/30] ring-buffer: Store bpage pointers into subbuf_ids
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[02-19 15:02]** [PATCH v12 03/30] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[02-19 15:02]** [PATCH v12 04/30] ring-buffer: Add non-consuming read for ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[02-19 15:02]** [PATCH v12 05/30] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[02-19 15:02]** [PATCH v12 06/30] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[02-19 15:02]** [PATCH v12 07/30] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[02-19 15:02]** [PATCH v12 08/30] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[02-19 15:02]** [PATCH v12 09/30] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[02-19 15:02]** [PATCH v12 10/30] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[02-19 15:02]** [PATCH v12 11/30] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[02-19 15:02]** [PATCH v12 12/30] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[02-19 15:02]** [PATCH v12 13/30] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[02-19 15:02]** [PATCH v12 14/30] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[02-19 15:02]** [PATCH v12 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[02-19 15:02]** [PATCH v12 16/30] Documentation: tracing: Add tracing remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[02-19 15:02]** [PATCH v12 17/30] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[02-19 15:02]** [PATCH v12 18/30] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[02-19 15:02]** [PATCH v12 19/30] KVM: arm64: Add PKVM_DISABLE_STAGE2_ON_PANIC
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[02-19 15:02]** [PATCH v12 20/30] KVM: arm64: Add clock support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[02-19 15:02]** [PATCH v12 21/30] KVM: arm64: Initialise hyp_nr_cpus for nVHE hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[02-19 15:02]** [PATCH v12 22/30] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[02-19 15:03]** [PATCH v12 23/30] KVM: arm64: Add tracing capability for the
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[02-19 15:03]** [PATCH v12 24/30] KVM: arm64: Add trace remote for the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[02-19 15:03]** [PATCH v12 25/30] KVM: arm64: Sync boot clock with the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
27. **[02-19 15:03]** [PATCH v12 26/30] KVM: arm64: Add trace reset to the nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
28. **[02-19 15:03]** [PATCH v12 27/30] KVM: arm64: Add event support to the nVHE/pKVM hyp
 and trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
29. **[02-19 15:03]** [PATCH v12 28/30] KVM: arm64: Add hyp_enter/hyp_exit events to
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
30. **[02-19 15:03]** [PATCH v12 29/30] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
31. **[02-19 15:03]** [PATCH v12 30/30] tracing: selftests: Add hypervisor trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
32. **[02-19 12:55]** Re: [PATCH v12 05/30] tracing: Introduce trace remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
33. **[02-19 12:55]** Re: [PATCH v12 07/30] tracing: Add non-consuming read to trace
 remotes
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
34. **[02-19 12:56]** Re: [PATCH v12 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
35. **[02-19 13:02]** Re: [PATCH v12 00/30] Tracefs support for pKVM
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
36. **[02-19 19:11]** Re: [PATCH v12 00/30] Tracefs support for pKVM
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context

**📧 邮件数**: 25 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 16 Feb 2026 13:09:59 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）环境下禁用 TRBE（Trace Buffer Unit）追踪缓冲区的补丁。补丁的主要目的是在运行虚拟机（guest）时，确保 TRBE 不会导致数据损坏和硬件锁死的问题。具体来说，当宿主机使用自托管 TRBE 时，补丁通过清除 TRBLIMITR_EL1.E 来禁止追踪生成。

在历史讨论中，参与者们探讨了 TRBE 的工作原理及其在虚拟化环境中的潜在问题，尤其是 TRFCR_EL1 和 TRBLIMITR_EL1 的相互作用。讨论中指出，TRBE 在虚拟机上下文中可能会进行不必要的地址转换，导致数据不一致。

在本周的新讨论中，参与者们对补丁的实现细节进行了深入探讨。Will Deacon 提出了补丁的初步实现，并指出该补丁尚未经过测试。Marc Zyngier 和其他参与者对 TRBE 的设计缺陷进行了批评，认为在当前架构下，支持虚拟机的 TRBE 是不切实际的。James Clark 进一步补充，当前的 TRBE 设计无法可靠地捕获虚拟机中的异常，因此在架构未修复之前，不应支持虚拟机的 TRBE。

总体而言，本周的讨论集中在补丁的细节和 TRBE 在虚拟化环境中的局限性上，参与者们一致认为需要对架构进行改进，以便在未来支持更可靠的追踪功能。

#### 📝 邮件列表

1. **[02-16 13:09]** [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Will Deacon <will@kernel.org>
2. **[02-16 14:29]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-16 15:05]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
4. **[02-16 15:13]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
5. **[02-16 15:51]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-16 15:53]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[02-16 16:10]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
8. **[02-16 16:49]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running in guest context
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-16 17:05]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
10. **[02-16 17:10]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
11. **[02-16 17:32]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
12. **[02-16 18:14]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
13. **[02-17 09:18]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
14. **[02-17 12:13]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
15. **[02-17 12:20]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
16. **[02-17 12:26]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
17. **[02-17 13:58]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
18. **[02-17 14:19]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
19. **[02-17 14:52]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
20. **[02-17 19:01]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
21. **[02-19 13:54]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Will Deacon <will@kernel.org>
22. **[02-19 18:58]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
23. **[02-19 19:06]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>
24. **[02-20 11:42]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: James Clark <james.clark@linaro.org>
25. **[02-20 15:48]** Re: [PATCH] KVM: arm64: Disable TRBE Trace Buffer Unit when running
 in guest context
   - 发件人: Leo Yan <leo.yan@arm.com>

---

### Thread 3: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 22 | **👥 参与者**: 5 | **📅 开始时间**: Tue,  3 Feb 2026 21:43:01 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 ARM MPAM（内存分区和监控）与 KVM/arm64 及 resctrl 的集成。历史讨论中，Ben Horgan 提出了一个包含 41 个补丁的系列，主要目的是完善 MPAM 驱动，特别是通过改进特性暴露的启发式方法，确保在不必要时不进行过度承诺。此外，补丁系列中还包括对 resctrl 的支持，特别是更新配置的辅助函数，以及对 'MB' 资源的支持。

在之前的讨论中，参与者们对补丁的功能进行了测试和反馈，指出了 MPAM 驱动在某些系统上对 MB 控制的限制，并讨论了如何在内存控制器上实现 MSC 支持。Zeng Heng 提供了测试结果，确认了多个功能的有效性，但也指出了一些未启用的功能。

在本周的新讨论中，Ben Horgan 对 Zeng Heng 的测试报告表示感谢，并询问了一些关于监控和 L3 缓存的具体问题。同时，参与者们讨论了 CDP（缓存数据保护）模拟的复杂性，并探讨了如何在 resctrl 中支持无 CPU 的 NUMA 节点。整体上，讨论集中在如何进一步完善 MPAM 的功能和支持上。

#### 📝 邮件列表

1. **[02-03 21:43]** [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[02-03 21:43]** [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[02-03 21:43]** [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[02-03 21:43]** [PATCH v4 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[02-03 21:43]** [PATCH v4 41/41] arm64: mpam: Add initial MPAM documentation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[02-05 16:50]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB'
 resource
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
7. **[02-05 17:05]** Re: [PATCH v4 41/41] arm64: mpam: Add initial MPAM documentation
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
8. **[02-10 06:20]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
9. **[02-13 07:02]** Re: [PATCH v4 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
10. **[02-13 15:38]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Zeng Heng <zengheng4@huawei.com>
11. **[02-14 09:29]** Re: [PATCH v4 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Zeng Heng <zengheng4@huawei.com>
12. **[02-14 17:40]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Zeng Heng <zengheng4@huawei.com>
13. **[02-14 18:39]** Re: [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update
 configuration
   - 发件人: Zeng Heng <zengheng4@huawei.com>
14. **[02-16 12:22]** Re: [PATCH v4 00/41] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[02-16 13:54]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
16. **[02-16 14:23]** Re: [PATCH v4 18/41] arm_mpam: resctrl: Implement helpers to update
 configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[02-18 16:22]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
18. **[02-18 16:40]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
19. **[02-18 16:42]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
20. **[02-18 17:02]** Re: [PATCH v4 41/41] arm64: mpam: Add initial MPAM documentation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[02-18 09:17]** Re: [PATCH v4 26/41] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
22. **[02-20 02:30]** Re: [PATCH v4 38/41] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>

---

### Thread 4: [PATCH 0/9] arm64: Fully disable configured-out features

**📧 邮件数**: 15 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Feb 2026 19:55:23 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构的补丁系列，旨在完全禁用已配置的特性，以解决在特性被禁用时仍然向用户空间暴露硬件状态的问题。

**原始补丁内容**：
Marc Zyngier 提出了一个补丁系列，共9个补丁，主要目的是通过引入新的宏（FTR_CONFIG()）来确保当某些特性（如 Pointer Auth、SVE、SME 等）在编译时未启用时，这些特性在内核的 ID 寄存器中不会被暴露，从而避免潜在的状态泄漏。

**之前讨论要点**：
在历史讨论中，Marc 指出当前的实现可能导致内核的不同部分对特性的认知不一致，尤其是在虚拟化环境中。此外，Marc 还提到，配置选项的增多可能会影响内核的可维护性，建议考虑更简化的配置方式。

**本周的新讨论与进展**：
本周的讨论集中在补丁的具体实现上。Marc 和 Fuad Tabba 讨论了如何优化结构体的内存布局，确保在处理特性时的安全性。Fuad 提出了对 FTR_ALL_HIDDEN 特性的处理建议，强调在某些情况下不应隐藏这些特性，以避免潜在的硬件错误。此外，Marc 也同意在处理 FTR_ALL_HIDDEN 特性时，应该采取更严格的措施，以防止在多核系统中出现状态不一致的问题。

总体来看，本周的讨论深化了对补丁实现的理解，并提出了具体的改进建议，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[02-19 19:55]** [PATCH 0/9] arm64: Fully disable configured-out features
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-19 19:55]** [PATCH 1/9] arm64: Add logic to fully remove features from sanitised id registers
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-19 19:55]** [PATCH 2/9] arm64: Convert CONFIG_ARM64_PTR_AUTH to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-19 19:55]** [PATCH 3/9] arm64: Convert CONFIG_ARM64_SVE to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-19 19:55]** [PATCH 4/9] arm64: Convert CONFIG_ARM64_SME to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[02-19 19:55]** [PATCH 5/9] arm64: Convert CONFIG_ARM64_GCS to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[02-19 19:55]** [PATCH 6/9] arm64: Convert CONFIG_ARM64_MTE to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[02-19 19:55]** [PATCH 7/9] arm64: Convert CONFIG_ARM64_POE to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[02-19 19:55]** [PATCH 8/9] arm64: Convert CONFIG_ARM64_BTI to FTR_CONFIG()
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[02-19 19:55]** [PATCH 9/9] arm64: Remove FTR_VISIBLE_IF_IS_ENABLED()
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[02-20 08:36]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[02-20 10:09]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from sanitised id registers
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[02-20 11:06]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[02-20 14:52]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from sanitised id registers
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[02-20 15:36]** Re: [PATCH 1/9] arm64: Add logic to fully remove features from
 sanitised id registers
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 5: [PATCH v2 00/10] KVM: selftests: Use kernel-style integer and
 g[vp]a_t types

**📧 邮件数**: 11 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 20 Feb 2026 00:42:13 +0000

#### 🤖 AI 总结

[AI 总结失败: Error code: 400 - {'error': {'message': "This model's maximum context length is 128000 tokens. However, your messages resulted in 240382 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}]
策略: 完整 thread (历史:0 新:11, 198684 tokens)

#### 📝 邮件列表

1. **[02-20 00:42]** [PATCH v2 00/10] KVM: selftests: Use kernel-style integer and
 g[vp]a_t types
   - 发件人: David Matlack <dmatlack@google.com>
2. **[02-20 00:42]** [PATCH v2 01/10] KVM: selftests: Use gva_t instead of vm_vaddr_t
   - 发件人: David Matlack <dmatlack@google.com>
3. **[02-20 00:42]** [PATCH v2 02/10] KVM: selftests: Use gpa_t instead of vm_paddr_t
   - 发件人: David Matlack <dmatlack@google.com>
4. **[02-20 00:42]** [PATCH v2 03/10] KVM: selftests: Use gpa_t for GPAs in Hyper-V selftests
   - 发件人: David Matlack <dmatlack@google.com>
5. **[02-20 00:42]** [PATCH v2 04/10] KVM: selftests: Use u64 instead of uint64_t
   - 发件人: David Matlack <dmatlack@google.com>
6. **[02-20 00:42]** [PATCH v2 05/10] KVM: selftests: Use s64 instead of int64_t
   - 发件人: David Matlack <dmatlack@google.com>
7. **[02-20 00:42]** [PATCH v2 06/10] KVM: selftests: Use u32 instead of uint32_t
   - 发件人: David Matlack <dmatlack@google.com>
8. **[02-20 00:42]** [PATCH v2 07/10] KVM: selftests: Use s32 instead of int32_t
   - 发件人: David Matlack <dmatlack@google.com>
9. **[02-20 00:42]** [PATCH v2 08/10] KVM: selftests: Use u16 instead of uint16_t
   - 发件人: David Matlack <dmatlack@google.com>
10. **[02-20 00:42]** [PATCH v2 09/10] KVM: selftests: Use s16 instead of int16_t
   - 发件人: David Matlack <dmatlack@google.com>
11. **[02-20 00:42]** [PATCH v2 10/10] KVM: selftests: Use u8 instead of uint8_t
   - 发件人: David Matlack <dmatlack@google.com>

---

### Thread 6: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI

**📧 邮件数**: 10 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 6 Feb 2026 18:42:19 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM64 架构中添加 CPU 特性 FEAT_LSUI 的补丁（PATCH v12 2/7）。该补丁旨在支持在特定条件下使用 FEAT_LSUI 特性。

在历史讨论中，参与者主要探讨了 FEAT_LSUI 与 FEAT_PAN 之间的依赖关系。Yeoreum Yun 提出，FEAT_LSUI 的实现似乎依赖于 FEAT_PAN 的存在，这引发了关于在没有 FEAT_PAN 的硬件上启用 FEAT_LSUI 的合理性讨论。Catalin Marinas 也指出，由于 ARM64 7.0 移除了 CONFIG_ARM64_PAN，禁用该特性变得更加复杂。他们讨论了如何在实现中处理这些依赖关系，以确保代码的兼容性和可读性。

在本周的新讨论中，Catalin Marinas 和 Yeoreum Yun 继续探讨了在处理 FEAT_LSUI 时的用户访问控制。Yeoreum Yun 表示可以在 FEAT_LSUI 路径中使用 uaccess_ttbr0_enable()，并讨论了是否需要引入新的函数 uaccess_enable_futex()。他们还提到需要在提交日志中明确 ABI 的轻微变化，并建议与用户空间（如 libc 和 Android）相关人员进行检查，以确保没有潜在问题。

总体来看，讨论围绕着如何正确实现和兼容 FEAT_LSUI 特性展开，确保在不同硬件条件下的稳定性和安全性。

#### 📝 邮件列表

1. **[02-06 18:42]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[02-09 18:57]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[02-10 09:54]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[02-10 16:14]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[02-10 16:45]** Re: [PATCH v12 6/7] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
6. **[02-10 17:01]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[02-10 17:17]** Re: [PATCH v12 6/7] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[02-16 18:04]** Re: [PATCH v12 6/7] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[02-16 18:24]** Re: [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[02-17 09:56]** Re: [PATCH v12 6/7] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 7: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 6 Feb 2026 14:59:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM KVM 中添加 `kvm-psci-version` vcpu 属性的补丁（PATCH v4 2/2）。该补丁旨在处理控制寄存器，以便在虚拟化环境中更好地支持 PSCI（电源状态协调接口）版本的管理。

在历史讨论中，参与者对补丁的合理性表示认可，并提出了一些技术细节上的问题。例如，讨论了在迁移时可能出现的 PSCI 版本不兼容的问题，以及如何确保 QEMU 在未来支持新的 PSCI 版本。Sebastian Ott 和 Peter Maydell 之间的交流中，明确了补丁中存在的潜在错误，并探讨了如何更好地实现 getter 和 setter 函数。

在本周的新讨论中，Peter Maydell 提出了对补丁的进一步要求，包括确保用户能够设置和读取 PSCI 版本的值，并在设置无效值时提供有用的错误信息。他还询问是否需要单独的 `kvm_prop_psci_version` 属性，或是否可以直接使用 `cpu->psci_version`。Sebastian Ott 对这些建议表示感谢，并已根据讨论内容实施了修改，发布了补丁的第六版（V6）。

#### 📝 邮件列表

1. **[02-06 14:59]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
2. **[02-11 16:37]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[02-11 15:43]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
4. **[02-11 17:04]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>
5. **[02-16 13:30]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
6. **[02-20 13:12]** Re: [PATCH v4 2/2] target/arm/kvm: add kvm-psci-version vcpu
 property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 8: [PATCH] KVM: arm64: Fix protected mode handling of pages larger than 4kB

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 22 Feb 2026 14:10:00 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下处理大于 4KB 页面时的保护模式问题的修复。原始的补丁旨在解决由于内存映射结构的变化而导致的非 4KB 页面支持失效的问题，具体表现为虚拟机无法启动，反复触发相同的错误。

在历史讨论中，Marc Zyngier 提出，由于在处理大页面时，某些寄存器返回的地址未能正确对齐，导致了页面映射失败。补丁通过强制对齐页面大小来解决这一问题，从而确保正确的物理页框号（PFN）被找到并映射到正确的位置。

在本周的新讨论中，参与者对补丁进行了审查和测试。Fuad Tabba 提出了代码中的一些小建议，如使用 ALIGN 宏来提高代码的可读性，并确认了补丁在使用不同页面大小（如 4KB、16KB 和 64KB）时的有效性。Marc Zyngier 进一步澄清了函数名称的细节，并确认了修复的有效性。

总体来看，本周的讨论集中在补丁的细节审查和测试结果上，参与者们对补丁的方向表示支持，并提出了一些改进建议。

#### 📝 邮件列表

1. **[02-22 14:10]** [PATCH] KVM: arm64: Fix protected mode handling of pages larger than 4kB
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-22 17:58]** Re: [PATCH] KVM: arm64: Fix protected mode handling of pages larger
 than 4kB
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[02-22 18:54]** Re: [PATCH] KVM: arm64: Fix protected mode handling of pages larger than 4kB
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-22 20:28]** Re: [PATCH] KVM: arm64: Fix protected mode handling of pages larger
 than 4kB
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 9: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 12 Feb 2026 10:48:47 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于支持 Arm CCA 的 KVM 的补丁（PATCH v12 00/46），主要涉及 arm64 架构。历史讨论中，Mathieu Poirier 提到之前的补丁在编译时存在问题，主要是因为函数 realm_configure_parameters() 未被调用。通过将该函数标记为 [[maybe_unused]]，解决了编译问题。此外，使用 FVP 模拟器启动包含 EDK2 的 Realm 时成功，但直接从 lkvm 启动内核时，挂载 initrd 失败。

在本周的新讨论中，Steven Price 对 kvmtool 代码的现状进行了评价，认为当前状态较差，存在许多临时性解决方案。他指出，realm_configure_parameters() 函数设置的哈希算法和 RPV 在 Linux 的更改中尚不支持，未来需要重新引入。Steven 还发现了 kvm_arm_realm_populate_ram() 中的一个简单错误，修复了源地址未更新的问题，并分享了代码修复补丁。最后，Mathieu 确认修复在他的环境中也有效，表示感谢。

总体来看，讨论围绕着补丁的编译问题、代码质量以及具体的 bug 修复展开，参与者积极交流并推动问题的解决。

#### 📝 邮件列表

1. **[02-12 10:48]** Re: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM
   - 发件人: Mathieu Poirier <mathieu.poirier@linaro.org>
2. **[02-16 12:33]** Re: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
3. **[02-16 14:27]** Re: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
4. **[02-17 10:47]** Re: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM
   - 发件人: Mathieu Poirier <mathieu.poirier@linaro.org>

---

### Thread 10: [PATCH v2 00/35] KVM: arm64: Add support for protected guest
 memory with pKVM

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 10 Feb 2026 10:58:03 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下添加对受保护来宾内存的支持，具体实现为 pKVM。原始的 patch 提出了这一功能的实现方案，旨在增强虚拟化环境中来宾内存的安全性。

在历史讨论中，参与者 Will Deacon 提出是否可以使用 QEMU 进行测试，还是需要真实的 SOC 平台来验证该 patch 的有效性。Trilok Soni 作为邮件的发起者，未对此进行详细回应。

在本周的新讨论中，Venkata Rao Kakani 表达了在应用该 patch 系列时遇到的问题，询问是否可以分享最新的提交，以便于他能够顺利应用。Fuad Tabba 随后回应，确认了提供的链接在 Linux 6.19-rc4 上是有效的。最终，Venkata 表示感谢，并确认问题已解决，能够成功应用该 patch。

总结来看，本周的讨论主要集中在 patch 应用过程中的技术问题上，参与者之间的沟通有效地解决了应用中的困难，推动了该功能的进一步测试与实施。

#### 📝 邮件列表

1. **[02-10 10:58]** Re: [PATCH v2 00/35] KVM: arm64: Add support for protected guest
 memory with pKVM
   - 发件人: Trilok Soni <trilokkumar.soni@oss.qualcomm.com>
2. **[02-16 16:28]** Re: [PATCH v2 00/35] KVM: arm64: Add support for protected guest
 memory with pKVM
   - 发件人: Venkata Rao Kakani <venkata.kakani@oss.qualcomm.com>
3. **[02-16 11:00]** Re: [PATCH v2 00/35] KVM: arm64: Add support for protected guest
 memory with pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[02-17 16:13]** Re: [PATCH v2 00/35] KVM: arm64: Add support for protected guest
 memory with pKVM
   - 发件人: Venkata Rao Kakani <venkata.kakani@oss.qualcomm.com>

---

### Thread 11: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during
 kvm_tlb_flush_vmid_range

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 9 Feb 2026 13:14:07 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 `kvm_tlb_flush_vmid_range` 函数中优化 `kvm_call_hyp` 的调用，以提高 ARM64 架构下的性能。最初的补丁（patch）由 eillon 提出，旨在减少在处理大范围 TLB 刷新时频繁调用 `kvm_call_hyp` 的次数，从而提升性能，尤其是在实时迁移场景中。

在历史讨论中，Marc Zyngier 对补丁提出了多个质疑，包括缺乏合并所需的 SoB（Signed-off-by）信息、没有提供足够的数据来证明该补丁在多种工作负载下的有效性，以及缺少可复现的测试描述。eillon 也回应了这些问题，指出 `kvm_tlb_flush_vmid_range` 的大部分开销来自于 `__tlb_switch_to_host()` 函数。

在本周的新讨论中，Marc Zyngier 再次质疑频繁调用 `kvm_call_hyp` 是否真的会导致成本增加，并要求提供具体的测试和配置，以便其他人能够复现 eillon 的发现。如果补丁确实能带来五倍的性能提升，复现应该不难。整体来看，讨论仍在继续，尚未达成共识。

#### 📝 邮件列表

1. **[02-09 13:14]** [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during
 kvm_tlb_flush_vmid_range
   - 发件人: yezhenyu (A) <yezhenyu2@huawei.com>
2. **[02-09 14:35]** Re: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during kvm_tlb_flush_vmid_range
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-12 20:02]** Re: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during
 kvm_tlb_flush_vmid_range
   - 发件人: yezhenyu (A) <yezhenyu2@huawei.com>
4. **[02-16 13:05]** Re: [RFC][PATCH] arm64: tlb: call kvm_call_hyp once during kvm_tlb_flush_vmid_range
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 12: [PATCH v6 42/44] KVM: VMX: Dedup code for adding MSR to VMCS's
 auto list

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Feb 2026 11:31:18 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch）“[PATCH v6 42/44] KVM: VMX: Dedup code for adding MSR to VMCS's auto list”，旨在优化 KVM 中将 MSR 添加到 VMCS 自动列表的代码，减少重复代码。

在历史讨论中，虽然没有具体提到，但可以推测该补丁是为了提高 KVM 的效率和可维护性，特别是在处理 MSR（模型特定寄存器）时的性能优化。

在本周的新讨论中，参与者 Namhyung Kim 和 Sean Christopherson 进行了技术交流。Namhyung 提出补丁中的一个问题，询问是否应该使用 `&m->host` 作为 `host_val`。Sean 随后确认这是一个错误，并解释了为何这个问题在测试中未被发现，主要是因为在实际操作中，只有 `MSR_IA32_PEBS_ENABLE` 会经过加载列表，而 VM 入口加载列表会使用来宾的值。Sean 还询问 Namhyung 是否在使用 PEBS 事件时遇到过问题。Namhyung 表示没有遇到问题，并确认将会发送修复补丁。

总体来看，本周的讨论主要集中在补丁的一个潜在问题上，参与者们积极探讨并计划后续的修复工作。

#### 📝 邮件列表

1. **[02-19 11:31]** Re: [PATCH v6 42/44] KVM: VMX: Dedup code for adding MSR to VMCS's
 auto list
   - 发件人: Namhyung Kim <namhyung@kernel.org>
2. **[02-20 08:46]** Re: [PATCH v6 42/44] KVM: VMX: Dedup code for adding MSR to VMCS's
 auto list
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[02-20 11:14]** Re: [PATCH v6 42/44] KVM: VMX: Dedup code for adding MSR to VMCS's
 auto list
   - 发件人: Namhyung Kim <namhyung@kernel.org>

---

### Thread 13: [PATCH v11 15/30] tracing: selftests: Add trace remote tests

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 5 Feb 2026 12:42:08 -0500

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（PATCH v11 15/30），其内容是为 Linux 内核的追踪功能添加远程测试（trace remote tests）。在历史讨论中，Vincent Donnefort 提到之前的测试存在失败情况，特别是与超管（hypervisor）相关的多个测试均被标记为“不支持”（UNSUPPORTED）。Steven Rostedt 在后续回复中提到，他在补丁的第11版中做了一些修改，尝试通过将 CPU 下线来解决问题，但似乎效果不佳。

在本周的新讨论中，Vincent Donnefort 更新了测试结果，确认自己之前运行的是旧的测试。在运行更新后的测试后，他报告了新的结果，其中有5个测试通过，0个失败，0个未解决，5个未支持的测试。具体来说，新的测试包括对远程缓冲区大小、远程重置、远程消费读取和远程卸载的测试，均成功通过。这表明补丁的更新有效提升了测试的通过率，虽然仍有部分超管相关的测试未被支持。整体来看，本周的讨论显示出补丁在功能验证方面取得了积极进展。

#### 📝 邮件列表

1. **[02-05 12:42]** Re: [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Steven Rostedt <rostedt@goodmis.org>
2. **[02-10 15:54]** Re: [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[02-19 09:36]** Re: [PATCH v11 15/30] tracing: selftests: Add trace remote tests
   - 发件人: Steven Rostedt <rostedt@goodmis.org>

---

### Thread 14: [PATCH v6 0/1] arm: add kvm-psci-version vcpu property

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 20 Feb 2026 12:56:55 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 ARM 架构下为 KVM 添加 PSCI 版本的 vcpu 属性的补丁（patch）。该补丁的目的是允许用户指定 KVM 提供给虚拟机的 PSCI 版本，以支持在不同默认 PSCI 版本的主机内核之间进行迁移。

在历史讨论中，补丁经历了多个版本的修改，主要集中在根据参与者的反馈进行调整，包括变量名称的更改、对代码的修复以及整合已经合并的补丁。补丁的核心内容是通过 KVM_REG_ARM_PSCI_VERSION FW 寄存器添加一个 vcpu 属性，允许用户设置 PSCI 版本，当前支持的版本包括 0.1、0.2、1.0、1.1、1.2 和 1.3。

在本周的新讨论中，Sebastian Ott 提交了补丁的第六版，详细说明了补丁的实现和使用场景，并指出为了支持 PSCI v0.1，必须在某些情况下放弃对 KVM_CAP_ARM_PSCI_0_2 的初始化。补丁得到了 Eric Auger 的审核和测试支持，表明其功能的有效性和稳定性。整体来看，本周的讨论进一步确认了补丁的方向和实施细节，为后续的合并奠定了基础。

#### 📝 邮件列表

1. **[02-20 12:56]** [PATCH v6 0/1] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[02-20 12:56]** [PATCH v6 1/1] target/arm/kvm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 15: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 13 Feb 2026 14:16:19 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 `__delay()` 函数中强制使用 `CNTVCT_EL0` 的补丁（patch）。历史讨论中，Marc Zyngier 提出了这个补丁，目的是解决一个与 KVM 虚拟化相关的问题。当虚拟 CPU 被加载且 KVM 不处于 VHE 模式时，`CNTVOFF_EL2` 被设置为非零值，导致 `__delay()` 函数在读取计数器时使用了错误的虚拟计数器（CNTPCT_EL0），而不是应该使用的物理计数器（CNTVCT_EL0）。这个问题可能会影响系统的延迟操作。

在本周的新讨论中，Will Deacon 确认该补丁已被应用到 arm64 的开发分支（for-next/core），并表示感谢。这表明该补丁得到了认可并已进入开发流程，解决了之前讨论中提到的问题。整体来看，这一补丁的实施将有助于提升 KVM 在非 VHE 模式下的稳定性和性能。

#### 📝 邮件列表

1. **[02-13 14:16]** [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[02-19 13:27]** Re: [PATCH] arm64: Force the use of CNTVCT_EL0 in __delay()
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 16: [PATCH 00/10] KVM: selftests: Convert to kernel-style types

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 18 Feb 2026 13:06:07 -0800

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM 自测代码的一个补丁（PATCH 00/10），旨在将其转换为内核风格的类型。该补丁的目标是提高代码的一致性和可维护性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁得到了积极的反馈，尤其是来自 Paolo 的支持，他在上周的 PUCK 会议中表示赞同进行类型重命名。

在本周的新讨论中，参与者 Sean Christopherson 和 David Matlack 进行了进一步的交流。David 提到他会在接下来的一周内准备一个新的版本，以便在合并窗口关闭后尽快应用该补丁。Sean 也确认会尽快处理此事，表示感谢。这表明该补丁正在朝着被采纳的方向推进，且预计将在下一个版本中得到应用。整体来看，讨论氛围积极，补丁的实施进展顺利。

#### 📝 邮件列表

1. **[02-18 13:06]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[02-18 13:17]** Re: [PATCH 00/10] KVM: selftests: Convert to kernel-style types
   - 发件人: David Matlack <dmatlack@google.com>

---

### Thread 17: [PATCH v9 10/30] KVM: arm64: Document the KVM ABI for SME

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 9 Feb 2026 15:18:43 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，具体内容是文档化 SME（Scalable Matrix Extension）的 KVM ABI（应用二进制接口）。

在历史讨论中，Mark Brown 提出了对补丁中描述的内容存在不一致的问题，询问补丁的意图是什么。Peter Maydell 对此进行了回应，但未给出明确的结论。

在本周的新讨论中，Peter Maydell 表示，如果采用让所有内容依赖于 SVCR（System Vector Control Register）的状态的方式，那么补丁的更新虽然不如 SVCR.SM 紧迫，但为了保持一致性，仍然会进行更新。他感谢 Mark Brown 指出这一问题，并表示将会进行相应的修改。

总结来看，本周的讨论主要集中在如何处理补丁中的不一致性问题，并达成了更新补丁以确保一致性的共识。

#### 📝 邮件列表

1. **[02-09 15:18]** Re: [PATCH v9 10/30] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
2. **[02-16 17:55]** Re: [PATCH v9 10/30] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 18: [PATCH v5 0/2] arm: add kvm-psci-version vcpu property

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 11 Feb 2026 16:30:30 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于在 ARM 架构中添加 KVM PSCI 版本的虚拟 CPU 属性，具体内容由 Sebastian Ott 提出的补丁系列 [PATCH v5 0/2] 进行介绍。该补丁旨在通过 KVM_REG_ARM_PSCI_VERSION 固件寄存器请求特定的 PSCI 版本，以支持在默认 PSCI 版本不同的主机内核之间的迁移。

在历史讨论中，Sebastian 提到，为了支持 PSCI v0.1，需要在使用 KVM_CAP_ARM_PSCI_0_2 时放弃虚拟 CPU 初始化，或者可以将支持限制在版本 >=0.2。此补丁系列自 V4 版本以来，已经根据 Peter 的反馈进行了修改，并添加了 R-B 和 T-B。

在本周的新讨论中，Peter Maydell 更新了补丁的状态，指出补丁 1 已经合并到主干中，而补丁 2 的审查讨论仍在进行中，主要参考了补丁 V4 版本的讨论内容。整体来看，讨论进展顺利，补丁的实施正在推进中。

#### 📝 邮件列表

1. **[02-11 16:30]** [PATCH v5 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[02-16 13:31]** Re: [PATCH v5 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Peter Maydell <peter.maydell@linaro.org>

---

### Thread 19: [PATCH v1] KVM: arm64: Revert accidental drop of kvm_uninit_stage2_mmu()
 for non-NV VMs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 22 Feb 2026 08:33:52 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的一个补丁，主要涉及对 `kvm_uninit_stage2_mmu()` 函数的意外删除进行回退。

**原始问题**：在之前的提交中，commit 0c4762e26879 为了避免在非嵌套虚拟机（non-NV VMs）中出现 UBSAN（未定义行为检测器）错误，向多个函数中添加了早期返回。这一更改不小心影响了 `kvm_arch_flush_shadow_all()` 函数，导致其在处理非嵌套虚拟机时跳过了对 `kvm_uninit_stage2_mmu(kvm)` 的调用。

**之前讨论要点**：虽然邮件中没有详细的历史讨论记录，但可以推测，此问题的出现可能引发了对 KVM 内存管理和虚拟机生命周期管理的关注，尤其是在 pKVM 环境下，未能正确解除共享内存会导致宿主机在回收内存时出现问题。

**本周新讨论**：本周的邮件由 Fuad Tabba 提出，建议通过删除 `kvm_arch_flush_shadow_all()` 中的早期返回来修复该问题。该修复允许在嵌套 MMU 清理过程中正确调用 `kvm_uninit_stage2_mmu()`，从而避免了宿主机在处理内存时的错误。邮件中还提到，修复已经提交并附上了相关的代码更改。

总的来说，此次讨论集中在修复 KVM 中的一个内存管理问题，以确保在非嵌套虚拟机环境下的正常操作。

#### 📝 邮件列表

1. **[02-22 08:33]** [PATCH v1] KVM: arm64: Revert accidental drop of kvm_uninit_stage2_mmu()
 for non-NV VMs
   - 发件人: Fuad Tabba <tabba@google.com>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: pKVM breakage in mainline on n1sdp

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Feb 2026 19:08:59 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 N1SDP 平台上运行 pKVM 时出现的故障。Mark Brown 提出了一个问题，描述了在主线内核中运行 kvm-unit-tests 时遇到的错误，特别是在 pKVM 模式下的 pmu-mem-access 测试中出现了警告和崩溃信息。与 VHE 模式相比，N1SDP 在 pKVM 模式下表现不佳。

在之前的讨论中，Marc Zyngier 对缺乏版本信息表示不满，并指出他在 Altra 平台上运行相同测试时没有遇到问题。他提到 KUT 的一些 PMU 测试在受保护模式下失败，可能与 PMU 异常的路由有关。他还提到，使用 16kB 页的主机在受保护模式下表现异常，可能导致测试无法正常进行。

本周的新讨论中，Marc Zyngier 进一步确认了问题与主线内核的版本有关，并表示需要调查是否与其他已知问题相关。Fuad Tabba 提出了一个可能的修复方案，并表示感谢大家的关注和帮助。整体来看，讨论集中在识别和解决 N1SDP 上 pKVM 模式故障的问题上。

#### 📝 邮件列表

1. **[02-20 19:08]** pKVM breakage in mainline on n1sdp
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[02-21 10:33]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[02-21 10:38]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[02-21 12:35]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[02-21 13:16]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[02-21 13:42]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[02-22 08:34]** Re: pKVM breakage in mainline on n1sdp
   - 发件人: Fuad Tabba <tabba@google.com>

---

