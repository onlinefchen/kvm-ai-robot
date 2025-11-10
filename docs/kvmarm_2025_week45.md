# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-11-10 00:23:47

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 259
- **总 Thread 数**: 21
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 20 threads (257 邮件)
- **GIT PULL**: 1 threads (2 邮件)

---

## 📌 PATCH

共 20 个 thread

---

### Thread 1: [PATCH v2 00/45] KVM: arm64: Add LR overflow infrastructure

**📧 邮件数**: 46 | **👥 参与者**: 1 | **📅 开始时间**: Sun,  9 Nov 2025 17:15:34 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的 LR（Link Register）溢出处理的补丁系列。以下是对讨论内容的总结：

1. **原始补丁内容**：
   本次补丁系列的主题是「添加 LR 溢出基础设施」，主要针对 KVM 的 ARM64 实现，旨在修复与 GIC（通用中断控制器）相关的多个 bug，并优化中断处理。补丁包括对 GICv3 和 GICv2 的支持，特别是在处理中断溢出时的逻辑。

2. **历史讨论要点**：
   之前的讨论集中在如何有效管理中断，尤其是在 LR 溢出时的处理机制。参与者指出，LR 的数量有限，而中断的数量可能会超过这一限制，因此需要一种机制来处理这些溢出中断。讨论中提到的关键点包括如何确保优先级高的中断能够被及时处理，以及如何在不同的 CPU 上协调中断状态。

3. **本周的新讨论与进展**：
   本周的讨论中，Marc Zyngier 提出了多个补丁，详细阐述了如何在 GICv3 和 GICv2 中实现 LR 溢出处理，包括：
   - 通过 ICV_DIR_EL1 进行中断去激活的处理。
   - 增强对 GICv2 SGI（共享中断）的处理，确保在去激活时考虑源 CPU。
   - 引入新的自测用例，以验证在不同情况下的中断处理逻辑。
   - 讨论了如何在中断处理过程中避免不必要的广播 IPIs（中断请求），以提高性能。

整体而言，本周的讨论围绕如何在 KVM 中实现更高效的中断管理展开，特别是在面对 LR 溢出和多核 CPU 环境下的挑战。

#### 📝 邮件列表

1. **[11-09 17:15]** [PATCH v2 00/45] KVM: arm64: Add LR overflow infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-09 17:15]** [PATCH v2 01/45] irqchip/gic: Add missing GICH_HCR control bits
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-09 17:15]** [PATCH v2 02/45] irqchip/gic: Expose CPU interface VA to KVM
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-09 17:15]** [PATCH v2 03/45] irqchip/apple-aic: Spit out ICH_MISR_EL2 value on spurious vGIC MI
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-09 17:15]** [PATCH v2 04/45] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[11-09 17:15]** [PATCH v2 05/45] KVM: arm64: GICv3: Detect and work around the lack of ICV_DIR_EL1 trapping
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-09 17:15]** [PATCH v2 06/45] KVM: arm64: Repack struct vgic_irq fields
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[11-09 17:15]** [PATCH v2 07/45] KVM: arm64: Add tracking of vgic_irq being present in a LR
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[11-09 17:15]** [PATCH v2 08/45] KVM: arm64: Add LR overflow handling documentation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[11-09 17:15]** [PATCH v2 09/45] KVM: arm64: GICv3: Drop LPI active state when folding LRs
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[11-09 17:15]** [PATCH v2 10/45] KVM: arm64: GICv3: Preserve EOIcount on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[11-09 17:15]** [PATCH v2 11/45] KVM: arm64: GICv3: Decouple ICH_HCR_EL2 programming from LRs
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[11-09 17:15]** [PATCH v2 12/45] KVM: arm64: GICv3: Extract LR folding primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[11-09 17:15]** [PATCH v2 13/45] KVM: arm64: GICv3: Extract LR computing primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[11-09 17:15]** [PATCH v2 14/45] KVM: arm64: GICv2: Preserve EOIcount on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[11-09 17:15]** [PATCH v2 15/45] KVM: arm64: GICv2: Decouple GICH_HCR programming from LRs being loaded
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[11-09 17:15]** [PATCH v2 16/45] KVM: arm64: GICv2: Extract LR folding primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[11-09 17:15]** [PATCH v2 17/45] KVM: arm64: GICv2: Extract LR computing primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[11-09 17:15]** [PATCH v2 18/45] KVM: arm64: Compute vgic state irrespective of the number of interrupts
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[11-09 17:15]** [PATCH v2 19/45] KVM: arm64: Eagerly save VMCR on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[11-09 17:15]** [PATCH v2 20/45] KVM: arm64: Revamp vgic maintenance interrupt configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[11-09 17:15]** [PATCH v2 21/45] KVM: arm64: Turn kvm_vgic_vcpu_enable() into kvm_vgic_vcpu_reset()
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[11-09 17:15]** [PATCH v2 22/45] KVM: arm64: Make vgic_target_oracle() globally available
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[11-09 17:15]** [PATCH v2 23/45] KVM: arm64: Invert ap_list sorting to push active interrupts out
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[11-09 17:15]** [PATCH v2 24/45] KVM: arm64: Move undeliverable interrupts to the end of ap_list
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[11-09 17:15]** [PATCH v2 25/45] KVM: arm64: Use MI to detect groups being enabled/disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[11-09 17:16]** [PATCH v2 26/45] KVM: arm64: GICv3: Handle LR overflow when EOImode==0
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[11-09 17:16]** [PATCH v2 27/45] KVM: arm64: GICv3: Handle deactivation via ICV_DIR_EL1 traps
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[11-09 17:16]** [PATCH v2 28/45] KVM: arm64: GICv3: Add GICv2 SGI handling to deactivation primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[11-09 17:16]** [PATCH v2 29/45] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[11-09 17:16]** [PATCH v2 30/45] KVM: arm64: GICv3: Add SPI tracking to handle asymmetric deactivation
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[11-09 17:16]** [PATCH v2 31/45] KVM: arm64: GICv3: Handle in-LR deactivation when possible
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[11-09 17:16]** [PATCH v2 32/45] KVM: arm64: GICv3: Avoid broadcast kick on CPUs lacking TDIR
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[11-09 17:16]** [PATCH v2 33/45] KVM: arm64: GICv2: Handle LR overflow when EOImode==0
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[11-09 17:16]** [PATCH v2 34/45] KVM: arm64: GICv2: Handle deactivation via GICV_DIR traps
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[11-09 17:16]** [PATCH v2 35/45] KVM: arm64: GICv2: Always trap GICV_DIR register
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[11-09 17:16]** [PATCH v2 36/45] KVM: arm64: selftests: gic_v3: Add irq group setting helper
   - 发件人: Marc Zyngier <maz@kernel.org>
38. **[11-09 17:16]** [PATCH v2 37/45] KVM: arm64: selftests: gic_v3: Disable Group-0 interrupts by default
   - 发件人: Marc Zyngier <maz@kernel.org>
39. **[11-09 17:16]** [PATCH v2 38/45] KVM: arm64: selftests: vgic_irq: Fix GUEST_ASSERT_IAR_EMPTY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
40. **[11-09 17:16]** [PATCH v2 39/45] KVM: arm64: selftests: vgic_irq: Change configuration before enabling interrupt
   - 发件人: Marc Zyngier <maz@kernel.org>
41. **[11-09 17:16]** [PATCH v2 40/45] KVM: arm64: selftests: vgic_irq: Exclude timer-controlled interrupts
   - 发件人: Marc Zyngier <maz@kernel.org>
42. **[11-09 17:16]** [PATCH v2 41/45] KVM: arm64: selftests: vgic_irq: Remove LR-bound limitation
   - 发件人: Marc Zyngier <maz@kernel.org>
43. **[11-09 17:16]** [PATCH v2 42/45] KVM: arm64: selftests: vgic_irq: Perform EOImode==1 deactivation in ack order
   - 发件人: Marc Zyngier <maz@kernel.org>
44. **[11-09 17:16]** [PATCH v2 43/45] KVM: arm64: selftests: vgic_irq: Add asymmetric SPI deaectivation test
   - 发件人: Marc Zyngier <maz@kernel.org>
45. **[11-09 17:16]** [PATCH v2 44/45] KVM: arm64: selftests: vgic_irq: Add Group-0 enable test
   - 发件人: Marc Zyngier <maz@kernel.org>
46. **[11-09 17:16]** [PATCH v2 45/45] KVM: arm64: selftests: vgic_irq: Add timer deactivation test
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH 00/33] KVM: arm64: Add LR overflow infrastructure

**📧 邮件数**: 40 | **👥 参与者**: 4 | **📅 开始时间**: Mon,  3 Nov 2025 16:54:44 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构下的 GIC（通用中断控制器）实现的多个补丁，主要集中在添加 LR（列表寄存器）溢出处理机制上。

**原始问题/补丁内容**：
Marc Zyngier 提出的补丁系列（共33个补丁）旨在解决 KVM 中 GICv3 的 LR 溢出问题，尤其是在处理大量中断时，LR 的数量可能不足以容纳所有中断，导致系统出现死锁或中断丢失的情况。

**之前讨论要点**：
历史讨论中提到，现有的 vgic 实现未能正确处理中断的优先级和状态，特别是在中断数量超过 LR 数量时，系统表现不佳。补丁的复杂性在于需要重新排序中断、处理不同的中断模式（如 EOImode），以及确保在不同 CPU 之间的中断状态一致性。

**本周新讨论/进展**：
本周的讨论主要集中在补丁的具体实现上，包括：
1. 增加了对 GICv2 和 GICv3 的中断去激活处理，确保在 EOImode 为 0 时能够正确处理未能进入 LR 的中断。
2. 讨论了如何通过维护中断的溢出列表来管理中断的去激活，确保系统在处理大量中断时的稳定性。
3. 解决了 GICv2 SGI（共享中断）的特殊处理需求，确保在去激活时考虑源 CPU。
4. 讨论了在不同 CPU 上处理 SPIs（共享外部中断）时的复杂性，确保所有 CPU 的状态一致。

总的来说，本周的讨论推动了补丁的完善，确保在复杂的中断处理场景下，KVM 的稳定性和性能得到提升。

#### 📝 邮件列表

1. **[11-03 16:54]** [PATCH 00/33] KVM: arm64: Add LR overflow infrastructure
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-03 16:54]** [PATCH 01/33] irqchip/gic: Add missing GICH_HCR control bits
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-03 16:54]** [PATCH 02/33] irqchip/gic: Expose CPU interface VA to KVM
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[11-03 16:54]** [PATCH 03/33] irqchip/apple-aic: Spit out ICH_MIDR_EL2 value on spurious vGIC MI
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-03 16:54]** [PATCH 04/33] KVM: arm64: Turn vgic-v3 errata traps into a patched-in constant
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[11-03 16:54]** [PATCH 05/33] KVM: arm64: GICv3: Detect and work around the lack of ICV_DIR_EL1 trapping
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[11-03 16:54]** [PATCH 06/33] KVM: arm64: Repack struct vgic_irq fields
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[11-03 16:54]** [PATCH 07/33] KVM: arm64: Add tracking of vgic_irq being present in a LR
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[11-03 16:54]** [PATCH 08/33] KVM: arm64: Add LR overflow handling documentation
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[11-03 16:54]** [PATCH 09/33] KVM: arm64: GICv3: Drop LPI active state when folding LRs
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[11-03 16:54]** [PATCH 10/33] KVM: arm64: GICv3: Preserve EOIcount on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[11-03 16:54]** [PATCH 11/33] KVM: arm64: GICv3: Decouple ICH_HCR_EL2 programming from LRs
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[11-03 16:54]** [PATCH 12/33] KVM: arm64: GICv3: Extract LR folding primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[11-03 16:54]** [PATCH 13/33] KVM: arm64: GICv3: Extract LR computing primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[11-03 16:54]** [PATCH 14/33] KVM: arm64: GICv2: Preserve EOIcount on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[11-03 16:54]** [PATCH 15/33] KVM: arm64: GICv2: Decouple GICH_HCR programming from LRs being loaded
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[11-03 16:55]** [PATCH 16/33] KVM: arm64: GICv2: Extract LR folding primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[11-03 16:55]** [PATCH 17/33] KVM: arm64: GICv2: Extract LR computing primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[11-03 16:55]** [PATCH 18/33] KVM: arm64: Compute vgic state irrespective of the number of interrupts
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[11-03 16:55]** [PATCH 19/33] KVM: arm64: Eagerly save VMCR on exit
   - 发件人: Marc Zyngier <maz@kernel.org>
21. **[11-03 16:55]** [PATCH 20/33] KVM: arm64: Revamp vgic maintenance interrupt configuration
   - 发件人: Marc Zyngier <maz@kernel.org>
22. **[11-03 16:55]** [PATCH 21/33] KVM: arm64: Make vgic_target_oracle() globally available
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[11-03 16:55]** [PATCH 22/33] KVM: arm64: Invert ap_list sorting to push active interrupts out
   - 发件人: Marc Zyngier <maz@kernel.org>
24. **[11-03 16:55]** [PATCH 23/33] KVM: arm64: Move undeliverable interrupts to the end of ap_list
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[11-03 16:55]** [PATCH 24/33] KVM: arm64: Use MI to detect groups being enabled/disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[11-03 16:55]** [PATCH 25/33] KVM: arm64: Add AP-list overflow split/splice
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[11-03 16:55]** [PATCH 26/33] KVM: arm64: GICv3: Handle LR overflow when EOImode==0
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[11-03 16:55]** [PATCH 27/33] KVM: arm64: GICv3: Handle deactivation via ICV_DIR_EL1 traps
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[11-03 16:55]** [PATCH 28/33] KVM: arm64: GICv3: Add GICv2 SGI handling to deactivation primitive
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[11-03 16:55]** [PATCH 29/33] KVM: arm64: GICv3: Set ICH_HCR_EL2.TDIR when interrupts overflow LR capacity
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[11-03 16:55]** [PATCH 30/33] KVM: arm64: GICv2: Handle LR overflow when EOImode==0
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[11-03 16:55]** [PATCH 31/33] KVM: arm64: GICv2: Handle deactivation via GICV_DIR traps
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[11-03 16:55]** [PATCH 32/33] KVM: arm64: GICv2: Always trap GICV_DIR register
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[11-03 16:55]** [PATCH 33/33] KVM: arm64: GICv3: Add SPI tracking to handle asymmetric deactivation
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[11-04 16:50]** Re: [PATCH 05/33] KVM: arm64: GICv3: Detect and work around the lack
 of ICV_DIR_EL1 trapping
   - 发件人: Yao Yuan <yaoyuan@linux.alibaba.com>
36. **[11-04 09:04]** Re: [PATCH 05/33] KVM: arm64: GICv3: Detect and work around the lack of ICV_DIR_EL1 trapping
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[11-04 17:40]** Re: [PATCH 05/33] KVM: arm64: GICv3: Detect and work around the lack
 of ICV_DIR_EL1 trapping
   - 发件人: Yao Yuan <yaoyuan@linux.alibaba.com>
38. **[11-04 19:13]** Re: [PATCH 03/33] irqchip/apple-aic: Spit out ICH_MIDR_EL2 value on
 spurious vGIC MI
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
39. **[11-05 10:01]** Re: [PATCH 05/33] KVM: arm64: GICv3: Detect and work around the lack
 of ICV_DIR_EL1 trapping
   - 发件人: kernel test robot <lkp@intel.com>
40. **[11-05 11:31]** Re: [PATCH 05/33] KVM: arm64: GICv3: Detect and work around the lack of ICV_DIR_EL1 trapping
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH v8 00/28] Tracefs support for pKVM

**📧 邮件数**: 29 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  7 Nov 2025 09:38:12 +0000

#### 🤖 AI 总结

本邮件讨论主题为「[PATCH v8 00/28] Tracefs 支持 pKVM」，主要围绕为 pKVM 超级管理程序添加 Tracefs 支持的补丁系列。以下是讨论的主要内容：

1. **原始补丁/问题内容**：
   该补丁系列旨在为 pKVM 超级管理程序提供 Tracefs 支持，以便于调试和性能分析。补丁引入了新的接口和数据结构，允许在内核和超管之间共享跟踪事件和缓冲区。

2. **之前讨论要点**：
   在历史讨论中，补丁的设计考虑了如何在保护模式下实现有效的事件跟踪，确保内核能够读取超管生成的跟踪数据。此外，补丁还讨论了如何处理环形缓冲区的读写操作，以及如何在不同 CPU 上管理这些操作。

3. **本周的新讨论、进展或结论**：
   本周的讨论主要集中在补丁的具体实现上，包括：
   - 引入了新的环形缓冲区接口和 Tracefs 目录结构，以支持远程跟踪。
   - 增加了对 pKVM 超级管理程序的事件支持，允许通过 Tracefs 接口触发事件。
   - 进行了自测事件的添加，确保在 Tracefs 中可以触发和读取事件。
   - 讨论了如何在 pKVM 超级管理程序中实现时钟同步和重置功能，以便更好地跟踪和管理事件。

总体来看，本周的讨论展示了补丁的逐步完善和对 pKVM 超级管理程序跟踪功能的深入实现，预计将显著提升调试和性能分析的能力。

#### 📝 邮件列表

1. **[11-07 09:38]** [PATCH v8 00/28] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[11-07 09:38]** [PATCH v8 01/28] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[11-07 09:38]** [PATCH v8 02/28] ring-buffer: Store bpage pointers into subbuf_ids
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[11-07 09:38]** [PATCH v8 03/28] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[11-07 09:38]** [PATCH v8 04/28] ring-buffer: Add non-consuming read for ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[11-07 09:38]** [PATCH v8 05/28] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[11-07 09:38]** [PATCH v8 06/28] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[11-07 09:38]** [PATCH v8 07/28] tracing: Add non-consuming read to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[11-07 09:38]** [PATCH v8 08/28] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[11-07 09:38]** [PATCH v8 09/28] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[11-07 09:38]** [PATCH v8 10/28] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[11-07 09:38]** [PATCH v8 11/28] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[11-07 09:38]** [PATCH v8 12/28] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[11-07 09:38]** [PATCH v8 13/28] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[11-07 09:38]** [PATCH v8 14/28] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[11-07 09:38]** [PATCH v8 15/28] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[11-07 09:38]** [PATCH v8 16/28] Documentation: tracing: Add tracing remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[11-07 09:38]** [PATCH v8 17/28] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[11-07 09:38]** [PATCH v8 18/28] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[11-07 09:38]** [PATCH v8 19/28] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[11-07 09:38]** [PATCH v8 20/28] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[11-07 09:38]** [PATCH v8 21/28] KVM: arm64: Add tracing capability for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[11-07 09:38]** [PATCH v8 22/28] KVM: arm64: Add trace remote for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[11-07 09:38]** [PATCH v8 23/28] KVM: arm64: Sync boot clock with the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[11-07 09:38]** [PATCH v8 24/28] KVM: arm64: Add trace reset to the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
26. **[11-07 09:38]** [PATCH v8 25/28] KVM: arm64: Add event support to the pKVM hyp and
 trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
27. **[11-07 09:38]** [PATCH v8 26/28] KVM: arm64: Add hyp_enter/hyp_exit events to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
28. **[11-07 09:38]** [PATCH v8 27/28] KVM: arm64: Add selftest event support to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
29. **[11-07 09:38]** [PATCH v8 28/28] tracing: selftests: Add pKVM trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 4: [PATCH v1 0/8] KVM: arm64: Fixes for guest CPU feature trapping and enabling

**📧 邮件数**: 21 | **👥 参与者**: 4 | **📅 开始时间**: Tue,  4 Nov 2025 12:58:58 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的多个修复补丁，主要集中在来宾 CPU 特性捕获和启用方面。

**原始补丁内容**：
该系列补丁包含八个部分，旨在修复来宾 vCPU 特性捕获和启用的逻辑错误，包括修正 MOPS 异常路由的反向逻辑、添加缺失的特性捕获（如 FEAT_NMI）以及确保支持的特性（如 FEAT_LS64）能够正确启用。此外，还对 vcpu_set_hcrx() 函数进行了简单重构，以提高可读性。

**之前讨论要点**：
在之前的讨论中，参与者对补丁的逻辑进行了审查，特别是关于 MOPS 异常的处理。有人指出，当前逻辑可能不符合预期，认为在某些情况下应将异常捕获到 EL2，而不是让来宾处理。对此，Fuad Tabba 表示会考虑反馈并调整补丁。

**本周新讨论与进展**：
本周的讨论主要围绕每个补丁的具体实现和逻辑修复展开。Fuad Tabba 对每个补丁进行了详细说明，并对一些逻辑错误进行了修正。参与者 Marc Zyngier 提出了一些关于如何更好地处理特性捕获的建议，强调应自动推导这些行为。最终，Fuad 表示将根据反馈进行相应的调整，并继续推进补丁的完善。整体来看，本周讨论积极，推动了补丁的进一步发展和完善。

#### 📝 邮件列表

1. **[11-04 12:58]** [PATCH v1 0/8] KVM: arm64: Fixes for guest CPU feature trapping and enabling
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[11-04 12:58]** [PATCH v1 1/8] KVM: arm64: Route MOPS exceptions to EL2 when guest
 lacks support
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[11-04 12:59]** [PATCH v1 2/8] KVM: arm64: Trap access to ALLINT if FEAT_NMI not
 supported by the guest
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[11-04 12:59]** [PATCH v1 3/8] KVM: arm64: Enable LS64 instructions when supported by guest
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[11-04 12:59]** [PATCH v1 4/8] KVM: arm64: Refactor vcpu_set_hcrx() to reduce indentation
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[11-04 12:59]** [PATCH v1 5/8] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[11-04 12:59]** [PATCH v1 6/8] KVM: arm64: Fix MTE flag initialization for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[11-04 12:59]** [PATCH v1 7/8] KVM: arm64: Prevent host from managing timer offsets
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[11-04 12:59]** [PATCH v1 8/8] KVM: arm64: Define FAR_MASK for faulting IPA offset
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[11-04 13:44]** Re: [PATCH v1 1/8] KVM: arm64: Route MOPS exceptions to EL2 when
 guest lacks support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
11. **[11-04 13:49]** Re: [PATCH v1 1/8] KVM: arm64: Route MOPS exceptions to EL2 when
 guest lacks support
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[11-04 15:15]** Re: [PATCH v1 2/8] KVM: arm64: Trap access to ALLINT if FEAT_NMI not supported by the guest
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[11-04 15:26]** Re: [PATCH v1 3/8] KVM: arm64: Enable LS64 instructions when supported by guest
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[11-04 15:30]** Re: [PATCH v1 2/8] KVM: arm64: Trap access to ALLINT if FEAT_NMI not
 supported by the guest
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[11-04 15:31]** Re: [PATCH v1 3/8] KVM: arm64: Enable LS64 instructions when
 supported by guest
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[11-04 17:22]** Re: [PATCH v1 2/8] KVM: arm64: Trap access to ALLINT if FEAT_NMI not supported by the guest
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[11-04 17:30]** Re: [PATCH v1 2/8] KVM: arm64: Trap access to ALLINT if FEAT_NMI not
 supported by the guest
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[11-04 17:50]** Re: [PATCH v1 5/8] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
19. **[11-04 17:56]** Re: [PATCH v1 5/8] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
20. **[11-04 18:03]** Re: [PATCH v1 5/8] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
21. **[11-04 19:04]** Re: [PATCH v1 5/8] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 5: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups

**📧 邮件数**: 16 | **👥 参与者**: 6 | **📅 开始时间**: Thu, 30 Oct 2025 13:09:23 -0700

#### 🤖 AI 总结

本邮件线程讨论了 KVM 的一系列补丁，主要集中在 TDX（可信执行环境）后填充路径的清理工作。原始补丁（PATCH v4 00/28）旨在解决 KVM 中的锁定问题，确保在处理与 TDX 相关的状态转换时，所有相关锁都被正确获取，以避免竞态条件和潜在的 KVM 错误。

在历史讨论中，Sean Christopherson 提出了补丁的背景，强调了在 TDX 的后填充钩子与 KVM 内部路径之间的锁定问题。补丁 26 和 27 主要关注确保在执行特定 I/O 控制命令时，获取所有必要的锁，以防止状态转换中的错误。

本周的新讨论中，参与者们对补丁进行了进一步的审查和讨论。Binbin Wu 对补丁 27 提出了细节上的建议，并表示将进行修改。Sean Christopherson 鼓励发送补丁的第二版以整合反馈。Mostafa Saleh 和 Jason Gunthorpe 则探讨了与 KVM 初始化顺序相关的 IOMMU 驱动加载问题，提出了在 KVM 初始化后再加载 SMMU 驱动的建议。

总体来看，本周讨论集中在补丁的细节修改和对 KVM 驱动加载顺序的优化建议上，显示出社区对提高 KVM 可靠性和性能的持续关注。

#### 📝 邮件列表

1. **[10-30 13:09]** [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-30 13:09]** [PATCH v4 26/28] KVM: TDX: Guard VM state transitions with "all" the locks
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[10-30 13:09]** [PATCH v4 27/28] KVM: TDX: Bug the VM if extending the initial
 measurement fails
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[10-31 16:26]** Re: [PATCH v4 26/28] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
5. **[10-31 17:28]** Re: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
6. **[10-31 10:34]** Re: [PATCH v4 26/28] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[11-03 09:36]** Re: [PATCH v4 26/28] KVM: TDX: Guard VM state transitions with "all"
 the locks
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
8. **[11-04 14:16]** Re: [PATCH v4 27/28] KVM: TDX: Bug the VM if extending the initial
 measurement fails
   - 发件人: Binbin Wu <binbin.wu@linux.intel.com>
9. **[11-04 09:58]** Re: [PATCH v4 00/28] KVM: x86/mmu: TDX post-populate cleanups
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[11-04 10:02]** Re: [PATCH v4 27/28] KVM: TDX: Bug the VM if extending the initial
 measurement fails
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[11-05 16:40]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Mostafa Saleh <smostafa@google.com>
12. **[11-05 13:12]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
13. **[11-06 11:06]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Mostafa Saleh <smostafa@google.com>
14. **[11-06 09:23]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
15. **[11-06 16:54]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Mostafa Saleh <smostafa@google.com>
16. **[11-06 13:16]** Re: [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM
 mode
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 6: [PATCH v7 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 15 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 7 Nov 2025 15:21:20 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是添加对Armv8.7引入的FEAT_{LS64, LS64_V}的支持及相关测试。该功能涉及单拷贝原子64字节加载和存储指令，旨在提高用户空间驱动程序的性能，特别是在直接与硬件交互时。

在历史讨论中，邮件未提供具体的背景信息，但本周的新讨论详细描述了七个补丁的内容和目的。补丁主要包括：
1. **补丁内容**：补丁添加了对FEAT_{LS64, LS64_V}的支持，包括在CPU功能列表中标识和启用这些特性，向用户空间暴露这些特性（通过HWCAP3和cpuinfo），以及相关的硬件能力测试。
2. **之前讨论要点**：虽然没有明确的历史讨论，但补丁的演变显示出对不同版本的重构和改进，特别是在处理虚拟机中的内存访问异常时。
3. **本周新讨论**：本周的讨论集中在补丁的具体实现和测试上，包括对KVM的支持，如何在用户空间处理特定指令的退出原因，以及对补丁顺序的建议。参与者对补丁的内容表示认可，并提出了一些小的改进建议。

总体而言，这一系列补丁旨在增强Linux内核对新硬件特性的支持，提升虚拟化环境中的性能和稳定性。

#### 📝 邮件列表

1. **[11-07 15:21]** [PATCH v7 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[11-07 15:21]** [PATCH v7 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B* outside of memslots
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
3. **[11-07 15:21]** [PATCH v7 2/7] KVM: arm64: Add documentation for KVM_EXIT_ARM_LDST64B
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
4. **[11-07 15:21]** [PATCH v7 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
5. **[11-07 15:21]** [PATCH v7 4/7] arm64: Provide basic EL2 setup for FEAT_{LS64, LS64_V} usage at EL0/1
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
6. **[11-07 15:21]** [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
7. **[11-07 15:21]** [PATCH v7 6/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the supported guest
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
8. **[11-07 15:21]** [PATCH v7 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
9. **[11-07 10:21]** Re: [PATCH v7 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64, LS64_V}
   - 发件人: Arnd Bergmann <arnd@arndb.de>
10. **[11-07 10:23]** Re: [PATCH v7 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Arnd Bergmann <arnd@arndb.de>
11. **[11-07 11:48]** Re: [PATCH v7 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B*
 outside of memslots
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
12. **[11-07 11:49]** Re: [PATCH v7 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B*
 outside of memslots
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
13. **[11-07 12:05]** Re: [PATCH v7 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
14. **[11-07 10:53]** Re: [PATCH v7 6/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the
 supported guest
   - 发件人: Oliver Upton <oupton@kernel.org>
15. **[11-07 10:57]** Re: [PATCH v7 0/7] Add support for FEAT_{LS64, LS64_V} and related
 tests
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 7: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map

**📧 邮件数**: 14 | **👥 参与者**: 5 | **📅 开始时间**: Fri, 31 Oct 2025 17:30:12 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（内核虚拟机）中 `guest_memfd` 的一个补丁，目的是增加一个标志以从直接映射中移除内存。补丁的编号为 PATCH v7 05/12。

**历史讨论**中，参与者讨论了 `can_set_direct_map` 函数的存在与否，尤其是在不同架构下的实现问题。Brendan Jackman 和 Mike Rapoport 提到了一些架构（如 PowerPC）可能没有实现该函数的 stub，导致在特定情况下可能出现问题。

**本周的新讨论**中，Aneesh Kumar K.V 指出某些函数实际上在执行 TLB 刷新操作。Brendan Jackman 和 Mike Rapoport 继续探讨 `can_set_direct_map` 的实现细节，讨论了在没有 `set_direct_map_*` 的架构中如何处理 `GUEST_MEMFD_FLAG_NO_DIRECT_MAP`。Nikita Kalyazin 提出了通过在 VM 进入时刷新 TLB 的方法，以确保不会出现过时的条目，并分享了性能测试结果。Ackerley Tng 进一步指出，当前的方案不能完全满足他们的用例，特别是在处理未预先填充的页面时。

总的来说，讨论围绕补丁的实现细节、架构兼容性以及如何优化 TLB 刷新性能展开，参与者们积极提出建议和解决方案。

#### 📝 邮件列表

1. **[10-31 17:30]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Brendan Jackman <jackmanb@google.com>
2. **[11-01 11:39]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
3. **[11-03 13:27]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Aneesh Kumar K.V <aneesh.kumar@kernel.org>
4. **[11-03 10:35]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Brendan Jackman <jackmanb@google.com>
5. **[11-03 12:50]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from
 direct map
   - 发件人: Mike Rapoport <rppt@kernel.org>
6. **[11-04 11:08]** Re: [PATCH v7 05/12] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Brendan Jackman <jackmanb@google.com>
7. **[11-07 07:29]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Ackerley Tng <ackerleytng@google.com>
8. **[11-07 15:54]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Brendan Jackman <jackmanb@google.com>
9. **[11-07 17:21]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
10. **[11-07 17:22]** Re: [PATCH v7 06/12] KVM: guest_memfd: add module param for disabling
 TLB flushing
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
11. **[11-07 17:23]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
12. **[11-07 17:37]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Brendan Jackman <jackmanb@google.com>
13. **[11-07 18:04]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Brendan Jackman <jackmanb@google.com>
14. **[11-07 18:11]** Re: [PATCH v7 00/12] Direct Map Removal Support for guest_memfd
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>

---

### Thread 8: [PATCH v11 0/9] support FEAT_LSUI

**📧 邮件数**: 14 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  6 Nov 2025 09:40:14 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于支持 Arm 架构新特性 FEAT_LSUI 的补丁集（PATCH v11 0/9）。FEAT_LSUI 允许特权级代码在不清除 PSTATE.PAN 位的情况下访问用户内存，从而优化了内核的加载/存储操作。

**补丁内容**：
该补丁集包括九个补丁，主要功能是支持 FEAT_LSUI，涉及到的内容包括：
1. 添加 CPU 特性检测（补丁 #1）。
2. 将 FEAT_LSUI 暴露给虚拟机（补丁 #2）。
3. 为 FEAT_LSUI 添加 Kconfig 配置（补丁 #4）。
4. 支持 futex 原子操作和用户 swpX 模拟（补丁 #5-#9）。

**历史讨论要点**：
在之前的讨论中，补丁经历了多次迭代，逐步完善了对 FEAT_LSUI 的支持，特别是对用户 swpX 操作的实现进行了重构，以减少对 PSTATE.PAN 的切换，从而降低潜在问题的发生。

**本周新讨论进展**：
本周的讨论主要集中在补丁的细节和性能优化上。参与者 Arnd Bergmann 提出对补丁的复杂性和性能影响的疑问，Yeoreum Yun 解释了使用 FEAT_LSUI 的主要目的是消除 PSTATE.PAN 切换带来的潜在问题，尽管这可能增加了代码复杂性。Yeoreum 还表示将根据反馈更新补丁描述，以更清晰地阐述补丁的目的和好处。

#### 📝 邮件列表

1. **[11-06 09:40]** [PATCH v11 0/9] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[11-06 09:40]** [PATCH v11 1/9] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[11-06 09:40]** [PATCH v11 2/9] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[11-06 09:40]** [PATCH v11 3/9] KVM: arm64: kselftest: set_id_regs: add test for FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[11-06 09:40]** [PATCH v11 4/9] arm64: Kconfig: Detect toolchain support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[11-06 09:40]** [PATCH v11 5/9] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[11-06 09:40]** [PATCH v11 6/9] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[11-06 09:40]** [PATCH v11 7/9] arm64: separate common LSUI definitions into lsui.h
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[11-06 09:40]** [PATCH v11 8/9] arm64: armv8_deprecated: convert user_swpX to inline function
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[11-06 09:40]** [PATCH v11 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[11-07 12:52]** Re: [PATCH v11 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for swpX
 emulation.
   - 发件人: Arnd Bergmann <arnd@arndb.de>
12. **[11-07 14:19]** Re: [PATCH v11 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for
 swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
13. **[11-07 15:24]** Re: [PATCH v11 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for swpX
 emulation.
   - 发件人: Arnd Bergmann <arnd@arndb.de>
14. **[11-07 15:57]** Re: [PATCH v11 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for
 swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 9: [PATCH v10 0/9] support FEAT_LSUI

**📧 邮件数**: 14 | **👥 参与者**: 2 | **📅 开始时间**: Mon,  3 Nov 2025 16:32:15 +0000

#### 🤖 AI 总结

本邮件讨论主题为支持 Armv9.6 的 FEAT_LSUI 特性，涉及一系列补丁（PATCH v10 0/9）。FEAT_LSUI 允许特权级代码在不清除 PSTATE.PAN 位的情况下访问用户内存，主要应用于 futex 原子操作和用户 swpX 模拟。

在历史讨论中，补丁经历了多个版本的迭代，逐步完善了对 FEAT_LSUI 的支持，包括添加 CPU 特性检测、向虚拟机暴露该特性、增加 Kconfig 配置、重构 futex 原子操作等。每个版本的补丁都在功能和代码结构上进行了优化。

本周的新讨论中，参与者 Yeoreum Yun 提交了补丁的最终版本，详细介绍了每个补丁的功能。补丁包括：
1. 添加 FEAT_LSUI 的 CPU 特性支持。
2. 向 KVM 虚拟机暴露 FEAT_LSUI。
3. 为 FEAT_LSUI 添加自测覆盖。
4. 更新 Kconfig 以检测工具链支持。
5. 重构 futex 原子操作以适应 FEAT_LSUI。
6. 支持使用 FEAT_LSUI 的 futex 操作。
7. 将通用的 LSUI 定义移入单独的头文件。
8. 将 user_swpX 宏转换为内联函数，并应用 FEAT_LSUI。

此外，Mark Brown 对部分补丁进行了审查，并提出了更新测试覆盖的建议。Yeoreum Yun 还发现使用 swpt 指令可能导致竞争条件，计划在下个版本中进行修正。整体来看，讨论围绕着对 FEAT_LSUI 的实现细节和潜在问题展开，显示出开发者们对代码质量和功能完整性的重视。

#### 📝 邮件列表

1. **[11-03 16:32]** [PATCH v10 0/9] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[11-03 16:32]** [PATCH v10 1/9] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[11-03 16:32]** [PATCH v10 2/9] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[11-03 16:32]** [PATCH v10 3/9] KVM: arm64: kselftest: set_id_regs: add test for FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[11-03 16:32]** [PATCH v10 4/9] arm64: Kconfig: Detect toolchain support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[11-03 16:32]** [PATCH v10 5/9] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[11-03 16:32]** [PATCH v10 6/9] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[11-03 16:32]** [PATCH v10 7/9] arm64: separate common LSUI definitions into lsui.h
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[11-03 16:32]** [PATCH v10 8/9] arm64: armv8_deprecated: convert user_swpX to inline function
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[11-03 16:32]** [PATCH v10 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[11-03 16:42]** Re: [PATCH v10 2/9] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[11-03 16:46]** Re: [PATCH v10 3/9] KVM: arm64: kselftest: set_id_regs: add test for
 FEAT_LSUI
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[11-04 10:55]** Re: [PATCH v10 3/9] KVM: arm64: kselftest: set_id_regs: add test for
 FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
14. **[11-04 11:01]** Re: [PATCH v10 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for
 swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 10: [PATCH v2 0/5] KVM: arm64: Fixes for guest CPU feature trapping and enabling

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Thu,  6 Nov 2025 14:44:12 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下的补丁系列，主要针对来宾 CPU 特性捕获和启用的修复。

**原始补丁/问题内容**：
补丁系列包含五个修复，旨在解决受保护虚拟机（pKVM）中与 Trace Buffer、MTE（内存标签扩展）标志初始化、定时器偏移管理等相关的问题。

**之前讨论要点**：
在补丁的早期版本中，参与者对 MOPS 补丁进行了讨论并决定放弃，同时也对粗粒度捕获的重构进行了讨论。针对 Trace Buffer 捕获的错误，Suzuki K Poulose 提出了反馈，促使对补丁进行修正。

**本周的新讨论和进展**：
1. Fuad Tabba 提交了补丁 v2，详细修复了 Trace Buffer 捕获的逻辑，确保只有在 Trace Buffer 不被支持时才会捕获相关寄存器的访问。
2. Oliver Upton 对补丁中的命名提出了建议，认为 FAR_MASK 的命名可能会引起混淆，建议使用更具描述性的名称。
3. 针对定时器偏移的管理，Oliver 还建议整合检查逻辑，以避免对受保护虚拟机的特殊处理，Fuad 同意并表示会在下次版本中进行调整。

整体来看，本周的讨论集中在补丁的细节修正和命名优化上，参与者积极反馈并推动补丁的完善。

#### 📝 邮件列表

1. **[11-06 14:44]** [PATCH v2 0/5] KVM: arm64: Fixes for guest CPU feature trapping and enabling
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[11-06 14:44]** [PATCH v2 1/5] KVM: arm64: Fix Trace Buffer trapping for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[11-06 14:44]** [PATCH v2 2/5] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[11-06 14:44]** [PATCH v2 3/5] KVM: arm64: Fix MTE flag initialization for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[11-06 14:44]** [PATCH v2 4/5] KVM: arm64: Prevent host from managing timer offsets
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[11-06 14:44]** [PATCH v2 5/5] KVM: arm64: Define FAR_MASK for fault IPA offset
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[11-06 16:28]** Re: [PATCH v2 1/5] KVM: arm64: Fix Trace Buffer trapping for
 protected VMs
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[11-07 15:12]** Re: [PATCH v2 5/5] KVM: arm64: Define FAR_MASK for fault IPA offset
   - 发件人: Oliver Upton <oupton@kernel.org>
9. **[11-07 15:21]** Re: [PATCH v2 4/5] KVM: arm64: Prevent host from managing timer
 offsets for protected VMs
   - 发件人: Oliver Upton <oupton@kernel.org>
10. **[11-09 19:51]** Re: [PATCH v2 4/5] KVM: arm64: Prevent host from managing timer
 offsets for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[11-09 19:51]** Re: [PATCH v2 5/5] KVM: arm64: Define FAR_MASK for fault IPA offset
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 11: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 22 Oct 2025 12:53:53 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的一个补丁（PATCH v3 04/25），该补丁旨在为将 guest_memfd 页框号映射到 TDP MMU 提供专用 API。历史讨论中，Yan Zhao 提出了在处理大页内转换时可能出现的 AB-BA 死锁问题，并指出在特定情况下会出现循环锁定依赖的警告。

在本周的新讨论中，Sean Christopherson 表达了对补丁的支持，并询问是否有人能继续推进此项工作。Yan Zhao 表示自己近期无法投入时间，建议其他人接手。同时，Sean 提出了一个修改建议，旨在解决警告问题，并更新了相关代码。Yan Zhao 随后也对代码进行了更新，增加了对 GUEST_MEMFD_FLAG_MMAP 的处理。

然而，Yan Zhao 对于在多个子系统中进行锁依赖处理表示担忧，并认为应将 gup() 调用移出 filemap_invalidate_lock() 之外，以避免潜在的 AB-BA 问题。总体来看，本周的讨论集中在补丁的细节修改和潜在的锁定问题上，参与者们积极探讨解决方案。

#### 📝 邮件列表

1. **[10-22 12:53]** Re: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
2. **[10-30 16:34]** Re: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
3. **[11-04 09:57]** Re: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[11-05 15:32]** Re: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
5. **[11-05 15:47]** Re: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Yan Zhao <yan.y.zhao@intel.com>
6. **[11-05 07:26]** Re: [PATCH v3 04/25] KVM: x86/mmu: Add dedicated API to map
 guest_memfd pfn into TDP MMU
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 12: [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 30 Oct 2025 12:27:04 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 在 arm64 架构下处理 ID_PFR1_EL1.GIC 的问题。历史讨论中，Marc Zyngier 提出了一个补丁系列（PATCH v2 0/3），旨在解决 Peter 报告的 GICv2 虚拟机恢复失败的问题，指出 ID_PFR1_EL1.GIC 不可写，而其 64 位等效项是可写的。这一问题在 6.12 版本中被引入，Marc 认为在 GIC 创建时调整 ID 寄存器比在运行时修复更为理想。

本周的新讨论中，Oliver Upton 对补丁进行了审核并表示支持。Suzuki K Poulose 提出了一个问题，询问为何所有三个补丁都有相同的修复标签，Marc 解释说这并非错误，因为并非所有修复都需要回溯到稳定版本。最终，Marc 确认这些补丁已被应用，并列出了每个补丁的提交信息，表明修复工作已顺利完成。整体来看，本周的讨论主要集中在补丁的审核和确认上，修复工作得到了积极的反馈。

#### 📝 邮件列表

1. **[10-30 12:27]** [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-06 17:34]** Re: [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[11-07 10:06]** Re: [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
4. **[11-08 11:24]** Re: [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[11-08 11:58]** Re: [PATCH v2 0/3] KVM: arm64: Fix handling of ID_PFR1_EL1.GIC
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v2 6/6] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may
 take LPI xarray lock

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 5 Nov 2025 17:37:10 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的 arm64 平台中 vgic-v3 组件的一个补丁，主要目的是指示 `vgic_put_irq()` 函数可能会在中断上下文中获取 LPI xarray 锁。

在历史讨论中，邮件没有提供具体的背景信息，但本周的讨论围绕着一个警告信息展开，该信息表明在特定情况下可能会出现不一致的锁状态，导致潜在的死锁问题。Zenghui Yu 提到在启动分配设备的来宾时，系统出现了锁依赖性（lockdep）警告，提示可能存在不安全的锁定场景。

本周的新讨论中，Marc Zyngier 和 Oliver Upton 讨论了 `might_lock()` 的使用，Marc 建议去掉这个检查，确保在中断上下文中不会获取 `lpi_xa.xa_lock`。Oliver 则认为保留这个检查是合理的，因为在某些情况下，`vgic_put_irq()` 可能会在中断上下文中获取锁。最终，Oliver 提出了一个补丁建议，修改了 `vgic_put_irq()` 函数的实现，以确保在适当的上下文中使用锁。

总结来说，本周的讨论集中在如何安全地管理锁定机制，以避免潜在的死锁，同时也提出了具体的代码修改建议。

#### 📝 邮件列表

1. **[11-05 17:37]** Re: [PATCH v2 6/6] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may
 take LPI xarray lock
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
2. **[11-05 10:28]** Re: [PATCH v2 6/6] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may take LPI xarray lock
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[11-05 16:46]** Re: [PATCH v2 6/6] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may
 take LPI xarray lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[11-05 16:58]** Re: [PATCH v2 6/6] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may
 take LPI xarray lock
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[11-06 11:34]** Re: [PATCH v2 6/6] KVM: arm64: vgic-v3: Indicate vgic_put_irq() may
 take LPI xarray lock
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 14: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 23 Oct 2025 10:16:05 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 自测中的未对齐 mmap 分配问题的补丁（PATCH v2 2/4）。该补丁旨在解决由于使用错误的 map_size 导致的 munmap() 失败问题，之前的讨论中提到，当前的未对齐 map_size 会导致 munmap() 失败，这在不同的后备存储测试中得到了验证。

在历史讨论中，Sean Christopherson 和 Jack Thomson 讨论了补丁的必要性和潜在影响，尤其是 munmap() 是否会静默失败的问题。Jack 提到，如果 munmap() 不会失败，那么这个补丁的实际作用值得商榷。

在本周的新讨论中，Sean 询问具体哪些测试失败，以及是否应该通过 vm_mem_add() 来解决测试问题。Jack 指出，测试失败主要发生在添加了更改后备页大小选项的 pre_faulting 测试中，并表示如果希望测试自行处理这些问题，他会在测试中进行更新。最终，Jack 强调了测试需要处理大小和对齐的问题，以避免库强制对齐可能掩盖测试缺陷的风险。

综上所述，讨论围绕如何妥善处理 KVM 自测中的 mmap 分配对齐问题展开，强调了测试的正确性和补丁的必要性。

#### 📝 邮件列表

1. **[10-23 10:16]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[10-28 11:44]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
3. **[11-03 13:08]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[11-04 11:40]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
5. **[11-04 12:19]** Re: [PATCH v2 2/4] KVM: selftests: Fix unaligned mmap allocations
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 15: [PATCH v2 0/2] KVM: arm64: vgic-v3: Even more locking fun

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  7 Nov 2025 10:48:45 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-v3（虚拟通用中断控制器）的锁机制改进，包含两个补丁（patch）。

**原始 patch/问题的内容**：
本次讨论的补丁主要针对 LPI（本地中断）xarray 的锁定顺序和释放保留槽的处理。补丁 v2 版本修复了在使用 LPI xarray 时可能导致的 IRQ（中断请求）上下文不一致的问题，并确保在调用 xa_release() 时能够正确释放锁。

**之前的讨论要点**：
在历史讨论中，参与者 Zenghui Yu 提出了在启用 lockdep 的情况下，KVM 客户机在分配设备时会出现错误的中断上下文，导致系统崩溃。为了解决这个问题，补丁 reinstates IRQ 锁定顺序，并更新了 lockdep 的提示。

**本周的新讨论、进展或结论**：
本周的讨论中，Oliver Upton 提交了两个补丁，分别是：
1. 恢复 LPI xarray 的 IRQ 锁定顺序，确保在特定情况下不会错误释放 IRQ 结构。
2. 修改 vgic_add_lpi() 函数，以便在调用 xa_release() 之前释放锁，避免在锁定状态下调用该函数。

最后，Marc Zyngier 确认已将这两个补丁应用到修复列表中，表示感谢。整体来看，本周的讨论集中在锁机制的改进上，以提高系统的稳定性和可靠性。

#### 📝 邮件列表

1. **[11-07 10:48]** [PATCH v2 0/2] KVM: arm64: vgic-v3: Even more locking fun
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[11-07 10:48]** [PATCH v2 1/2] KVM: arm64: vgic-v3: Reinstate IRQ lock ordering for LPI xarray
   - 发件人: Oliver Upton <oupton@kernel.org>
3. **[11-07 10:48]** [PATCH v2 2/2] KVM: arm64: vgic-v3: Release reserved slot outside of lpi_xa's lock
   - 发件人: Oliver Upton <oupton@kernel.org>
4. **[11-08 11:58]** Re: [PATCH v2 0/2] KVM: arm64: vgic-v3: Even more locking fun
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 3 Nov 2025 18:17:00 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理 SEA（Synchronous External Abort）时的 VM 退出到用户空间的补丁（PATCH v4 1/3）。该补丁旨在改进对 SEA 的处理，使其能够更有效地返回相关信息给用户空间。

在历史讨论中，参与者们关注了补丁的有效性，特别是针对 "Data Abort" 的检查是否合理，以及 PFAR_EL2 寄存器的值是否对处理 SEA 重要。讨论中提到，kvm_vcpu_get_fault_ipa 函数获取的是 HPFAR_EL2，这对于 S2 转换和 GPC 故障是有效的，但在其他情况下则不明确。

本周的新讨论中，Jose Marinho 和 Jiaqi Yan 进一步探讨了补丁的细节。Jiaqi Yan 确认 VNCR 位仅适用于 Data Abort，并表示不需要显式排除对指令中止的检查。同时，他提到用户空间和来宾不需要物理内存地址，因为主机物理地址应对用户空间隐藏。Marc Zyngier 则指出当前没有对 PFAR 的支持，也没有近期的计划来实现这一点，建议在 KVM 中引入 PFAR 之前，内核其他部分应先增加对其的支持。

总的来说，本周的讨论集中在补丁的细节和对 PFAR 支持的未来计划上，参与者们对如何处理 SEA 提出了不同的看法和建议。

#### 📝 邮件列表

1. **[11-03 18:17]** Re: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jose Marinho <jose.marinho@arm.com>
2. **[11-03 12:45]** Re: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[11-03 22:22]** Re: [PATCH v4 1/3] KVM: arm64: VM exit to userspace to handle SEA
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 17: [PATCH v9 0/5] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 29 Oct 2025 15:46:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 Armv8.8 SPE（可扩展性能监控）特性的补丁，主要集中在支持数据源过滤功能的实现上。

**原始补丁内容**：
James Clark 提出了一个补丁系列（PATCH v9），其中第一个补丁（PATCH v9 1/5）引入了 `perf_event_attr::config4` 字段，以支持新的数据源过滤功能。由于现有的 `perf_event_attr::configN` 字段已被占用，新增的 `config4` 字段将提供额外的 64 位事件过滤控制。

**之前讨论要点**：
在之前的讨论中，补丁经历了多次版本更新，修复了文档中的错误，并在最新的 `perf-tools-next` 基础上进行了重整。补丁得到了多位开发者的审查和测试，包括 Leo Yan 和 Ian Rogers。

**本周的新讨论**：
在本周的讨论中，Will Deacon 请求核心性能维护者对该扩展进行确认（ack/nak）。这一请求表明补丁已准备好进入进一步的审查阶段，期待得到社区的反馈和支持。

#### 📝 邮件列表

1. **[10-29 15:46]** [PATCH v9 0/5] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[10-29 15:46]** [PATCH v9 1/5] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
3. **[11-03 14:33]** Re: [PATCH v9 1/5] perf: Add perf_event_attr::config4
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 18: [PATCH] MAINTAINERS: Switch myself to using kernel.org address

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  6 Nov 2025 17:28:25 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于将维护者 Oliver Upton 的联系邮箱从 linux.dev 更改为 kernel.org。原始的补丁（patch）由 Oliver Upton 提交，目的是解决他在使用 linux.dev 邮箱时遇到的周期性问题，并希望在找到更合适的邮箱之前使用 kernel.org 地址。

在之前的讨论中，虽然没有具体的历史邮件记录，但可以推测出此补丁的提出是基于 Upton 对邮箱使用的实际困扰。

在本周的新讨论中，Oliver Upton 提交了补丁，并更新了 MAINTAINERS 文件和 .mailmap 文件，以反映其新的邮箱地址。Marc Zyngier 对此补丁进行了确认并表示已将其应用到修复中，感谢 Oliver 的贡献。此次更新标志着 Upton 在维护者列表中的联系信息得到了及时的修正。

#### 📝 邮件列表

1. **[11-06 17:28]** [PATCH] MAINTAINERS: Switch myself to using kernel.org address
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[11-08 11:59]** Re: [PATCH] MAINTAINERS: Switch myself to using kernel.org address
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH] KVM: arm64: vgic-v3: Reinstate IRQ lock ordering for LPI xarray

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  6 Nov 2025 17:29:44 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-v3（虚拟通用中断控制器）中恢复 LPI（本地中断）的 IRQ 锁顺序的补丁。

**原始补丁内容**：
补丁旨在解决在启用 lockdep（锁依赖检测）的情况下，运行 KVM 客户机时出现的 IRQ 上下文不一致问题。具体来说，当 LPI 的最后一个引用在注入缓存的 LPI 转换后被释放时，可能会导致不良的错误信息。补丁通过恢复 IRQ 锁的顺序并更新 lockdep 提示来解决此问题。

**之前讨论要点**：
虽然邮件中没有详细的历史讨论，但补丁的背景是由于 Zenghui Yu 报告的一个问题，指出在某些情况下可能会出现不一致的 IRQ 上下文。

**本周的新讨论与进展**：
本周的讨论中，Oliver Upton 提出了补丁的具体实现，并指出了补丁中对 IRQ 锁顺序的恢复。Zenghui Yu 在回复中提到，仍有一些地方在 IRQ 启用的情况下获取 lpi_xa.xa_lock，可能导致潜在问题。此外，他还指出在 vgic_add_lpi() 的错误路径中，xa_release() 可能会导致不良后果，因为它再次获取 xa_lock。整体来看，讨论集中在确保中断锁的正确使用和潜在问题的识别上。

#### 📝 邮件列表

1. **[11-06 17:29]** [PATCH] KVM: arm64: vgic-v3: Reinstate IRQ lock ordering for LPI xarray
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[11-07 17:46]** Re: [PATCH] KVM: arm64: vgic-v3: Reinstate IRQ lock ordering for LPI
 xarray
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 20: [PATCH V6 1/3] tools: header: arm64: Replace TCR_NFD[0|1] with
 TCR_EL1_NFD[0|1]

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 3 Nov 2025 17:31:27 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（PATCH V6 1/3），其内容是将 arm64 架构中的 TCR_NFD[0|1] 替换为 TCR_EL1_NFD[0|1]。该补丁旨在更新工具头文件，以反映最新的内核更改。

在之前的讨论中，邮件参与者 Anshuman Khandual 提出了一个问题，询问该文件是否通常由脚本自动更新，以保持与 arch/arm64/ 目录中的文件同步。对此，Catalin Marinas 进行了回应，确认通常是由 perf 工具的维护者（如 Arnaldo 或 Namhyung）负责同步这些头文件。

在本周的新讨论中，Catalin Marinas 和 Leo Yan 继续探讨了补丁的适用性。Leo Yan 表示，该补丁是可以发送的，并建议在内核更改合并后提醒 perf 维护者，以确保在工具中安全地采纳该更改。此外，Leo 还提到他已经使用该系列构建了 perf，并未发现任何问题。

总体来看，本周的讨论确认了补丁的有效性，并强调了与 perf 工具维护者的协调工作。

#### 📝 邮件列表

1. **[11-03 17:31]** Re: [PATCH V6 1/3] tools: header: arm64: Replace TCR_NFD[0|1] with
 TCR_EL1_NFD[0|1]
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
2. **[11-03 18:03]** Re: [PATCH V6 1/3] tools: header: arm64: Replace TCR_NFD[0|1] with
 TCR_EL1_NFD[0|1]
   - 发件人: Leo Yan <leo.yan@arm.com>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.18, take #2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sat,  8 Nov 2025 12:05:59 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 在 6.18 版本中的修复补丁（patch）。Marc Zyngier 提交了第二组修复，主要针对近期出现的一些回归问题，以及 pKVM 处理不可信数据的方式进行了改进。此外，还修复了一些自测试（selftests）中的问题，并更新了 Oliver 的电子邮件地址。

在历史讨论中没有相关内容，但本周的新讨论集中在 Marc 提交的修复补丁上。补丁包括多个核心修复，例如修复在没有内核中 IRQ 芯片时的陷阱回归、检查 pKVM 中的主机提供的不可信范围和偏移量、恢复 ID_PFR1_EL1 寄存器时的回归修复，以及在 LPI 未直接注入时的 vgic ITS 锁定问题。此外，还对自测试进行了修正，确保目标 CPU 编程和寄存器列表的正确性。

Paolo Bonzini 在本周的邮件中确认已拉取这些修复，表示感谢。这表明补丁已被接受并将纳入后续的开发中。

#### 📝 邮件列表

1. **[11-08 12:05]** [GIT PULL] KVM/arm64 fixes for 6.18, take #2
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[11-09 08:12]** Re: [GIT PULL] KVM/arm64 fixes for 6.18, take #2
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

